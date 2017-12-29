clear
clc
close all
 
% CREATE A RANDOM DATASET
rng(10)
nData = 10; % N
x = 2*(rand(1,nData)-.5);
 
xGrid = linspace(-1,1,100);
 
% DEFINE AND TARGET FUNCTION f(x)
f = inline('sin(pi*x)','x');
 
h = [];
h(1) = plot(xGrid,f(xGrid),'k','Linewidth',2);
xlabel('x')
hold on
 
% DEFINE AND DISPLAY y
noiseSTD = .1;
y = f(x) + noiseSTD*randn(size(x));
h(2) = scatter(x,y,'ko');
legend(h,{'f(x)','y'},'Location','Northwest');
 
% FIT POLYNOMIAL MODELS & DISPLAY
% (ASSUMING PREVIOUS PLOT ABOVE STILL AVAILABLE)
degree = [1,3,10];
theta = {};
cols = [.8 .05 0.05; 0.05 .6 0.05; 0.05 0.05 .6];
for iD = 1:numel(degree)
    figure(1)
    theta{iD} = polyfit(x,y,degree(iD));
    fit{iD} = polyval(theta{iD},xGrid);
    h(end+1) = plot(xGrid,fit{iD},'color',cols(iD,:),'Linewidth',2);
    xlim([-1 1])
    ylim([-1 1])
end
legend(h,'f(x)','y','g_1(x)','g_3(x)','g_{10}(x)','Location','Northwest')
 
% FIT MODELS TO K INDEPENDENT DATASETS
K = 50;
for iS = 1:K
    ySim = f(x) + noiseSTD*randn(size(x));
    for jD = 1:numel(degree)
        % FIT THE MODEL USING polyfit.m
        thetaTmp = polyfit(x,ySim,degree(jD));
        % EVALUATE THE MODEL FIT USING polyval.m
        simFit{jD}(iS,:) = polyval(thetaTmp,xGrid);
    end
end
 
% DISPLAY ALL THE MODEL FITS
h = [];
for iD = 1:numel(degree)
    figure(iD+1)
    hold on
    % PLOT THE FUNCTION FIT TO EACH DATASET
    for iS = 1:K
        h(1) = plot(xGrid,simFit{iD}(iS,:),'color',brighten(cols(iD,:),.6));
    end
    % PLOT THE AVERAGE FUNCTION ACROSS ALL FITS
    h(2) = plot(xGrid,mean(simFit{iD}),'color',cols(iD,:),'Linewidth',5);
    % PLOT THE UNDERLYING FUNCTION f(x)
    h(3) = plot(xGrid,f(xGrid),'color','k','Linewidth',3);
    % CALCULATE THE SQUARED ERROR AT EACH POINT, AVERAGED ACROSS ALL DATASETS
    squaredError = (mean(simFit{iD})-f(xGrid)).^2;
    % PLOT THE SQUARED ERROR
    h(4) = plot(xGrid,squaredError,'k--','Linewidth',3);
    uistack(h(2),'top')
    hold off
    axis square
    xlim([-1 1])
    ylim([-1 1])
    legend(h,{sprintf('Individual g_{%d}(x)',degree(iD)),'Mean of All Fits','f(x)','Squared Error'},'Location','WestOutside')
    title(sprintf('Model Order=%d',degree(iD)))
end
 
N = 25; % # OF OBSERVATIONS PER DATASET
K = 100;% # OF DATASETS
noiseSTD = .5; % NOISE STANDARDE DEV.
nTrain = ceil(N*.9); % # OF TRAINING POINTS
nPolyMax = 12; % MAXIMUM MODEL COMPLEXITY
 
% # INITIALIZE SOME VARIABLES
xGrid = linspace(-1,1,N);
meanPrediction = zeros(K,N);
thetaHat = {};
x = linspace(-1,1,N);
x = x(randperm(N));
for iS = 1:K % LOOP OVER DATASETS
 
    % CREATE OBSERVED DATA, y
    y = f(x) + noiseSTD*randn(size(x));
 
    % CREATE TRAINING SET
    xTrain = x(1:nTrain);
    yTrain = y(1:nTrain);
 
    % CREATE TESTING SET
    xTest = x(nTrain+1:end);
    yTest = y(nTrain+1:end);
 
    % FIT MODELS
    for jD = 1:nPolyMax
 
        % MODEL PARAMETER ESTIMATES
        thetaHat{jD}(iS,:) = polyfit(xTrain,yTrain,jD);
 
        % PREDICTIONS
        yHatTrain{jD}(iS,:) = polyval([thetaHat{jD}(iS,:)],xTrain); % TRAINING SET
        yHatTest{jD}(iS,:) = polyval([thetaHat{jD}(iS,:)],xTest);% TESTING SET
 
        % MEAN SQUARED ERROR
        trainErrors{jD}(iS) = mean((yHatTrain{jD}(iS,:) - yTrain).^2); % TRAINING
        testErrors{jD}(iS) = mean((yHatTest{jD}(iS,:) - yTest).^2); % TESTING
    end
end
 
% CALCULATE AVERAGE PREDICTION ERROR, BIAS, AND VARIANCE
for iD = 1:nPolyMax
    trainError(iD) = mean(trainErrors{iD});
    testError(iD) = mean(testErrors{iD});
    biasSquared(iD) = mean((mean(yHatTest{iD})-f(xTest)).^2);
    variance(iD) = mean(var(yHatTest{iD},1));
end
[~,bestModel] = min(testError);
 
% DISPLAY
figure;
hold on;
plot(testError,'k','Linewidth',2);
plot(biasSquared,'r','Linewidth',2);
plot(variance,'b','Linewidth',2);
plot(biasSquared + variance,'m-.','Linewidth',2);
yl = ylim;
plot([bestModel,bestModel],[yl(1),yl(2)],'k--');
xlim([1,nPolyMax]);
xlabel('Model Complexity (Polynomial Order)')
legend('Test Error','Bias^2','Variance','Bias^2+Var.','Best Model')
hold off;
 
% DISPLAY
figure, hold on;
plot(trainError,'g','Linewidth',2);
plot(testError,'k','Linewidth',2);
yl = ylim;
plot([bestModel,bestModel],[yl(1),yl(2)],'k--');
xlim([1,nPolyMax]);
xlabel('Model Complexity (Polynomial Order)')
legend('Train Error','Test Error','Best Model');
hold off;