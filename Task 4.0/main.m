m = 1000; % число объектов
X = rand([m 2]); % обучение
Y = (X(:,1)-0.5).^2 + (X(:,2)-0.5).^2 < 0.1; % классы
[tmp1 tmp2] = meshgrid(0:0.05:1, 0:0.05:1);
Xc = [tmp1(:) tmp2(:)]; % контроль
q = size(Xc, 1); % объектов в контроле
% алгоритмы
A = [];
% записаны по строкам
% A(i,1) - направление (1 или 2)
% A(i,2) =1 (>= порога) 0 (< порога)
% A(i,3) - порог
% A(i,4) - значение alpha
% визуализация
% scatter(X(:,1),X(:,2),20,Y,'filled')
scatter(X(Y>0,1), X(Y>0,2), 20, X(Y>0), 's', 'r');
hold on;
scatter(X(Y<=0,1), X(Y<=0,2), 20, X(Y<=0), 'o', 'b', 'filled');

% веса объектов
W = ones(size(Y))/m;

% просто инициализация (выделение памяти)
Y1 = zeros(size(Y));
Y2 = zeros(size(Y));

for I = 1:100 % просто построить 100 алгоритмов

 % выбор алгоритма
 % по первому направлению
 [Xs I] = sortrows(X, 1);
 Ys = Y(I);
 Ws = W(I);

 % приём для вычисления ошибки
- 122 - Дьяконов А.Г. Учебное пособие
 Y1(:) = 0;
 Y1(Ys==1) = Ws(Ys==1);
 Y1 = cumsum(Y1);

 Y2(:) = 0;
 Y2(Ys==0) = Ws(Ys==0);
 Y2 = cumsum(Y2(end:-1:1));
 Y2 = Y2(end:-1:1);

 Y2 = [0; Y1(1:end-1)] + Y2;

 [mx imx] = max(Y2);
 [mn imn] = min(Y2);

 if (mn<1-mx) a = [1 1 Xs(imn,1)]; e = mn;
 else a = [1 0 Xs(imx,1)]; e = 1 - mx;
 end;

 % по второму
 [Xs I] = sortrows(X,2);
 Ys = Y(I);
 Ws = W(I);

 % приём для вычисления ошибки
 Y1(:) = 0;
 Y1(Ys==1) = Ws(Ys==1);
 Y1 = cumsum(Y1);

 Y2(:) = 0;
 Y2(Ys==0) = Ws(Ys==0);
 Y2 = cumsum(Y2(end:-1:1));
 Y2 = Y2(end:-1:1);

 Y2 = [0; Y1(1:end-1)] + Y2;

 [mx imx] = max(Y2);
 [mn imn] = min(Y2);

 if (mn<1-mx) if (mn<e) a = [2 1 Xs(imn,2)]; e = mn; end;
 else if (1-mx<e) a = [2 0 Xs(imx,2)]; e = 1 - mx; end;
 end;

 % визуализация
 figure(1);
 if a(1)==1
 plot([abs(a(3)) abs(a(3))], [0 1], 'k', 'LineWidth', 2);
 else
 plot([0 1], [abs(a(3)) abs(a(3))], 'k', 'LineWidth', 2);
 end;

 % бустинг
 alpha = 0.5*log((1-e)/e); 
Глава 10. Объединение элементарных классификаторов - 123 -

 W = W.*exp( alpha*(1 - 2*( ((X(:,a(1))>=a(3))==a(2)) == Y )));
 W = W/sum(W);

 % добавление алгоритма
 A(end+1,:) = [a(1:3) alpha];

 % текущий классификатор
 h = (2*((Xc(:, A(:,1))>=repmat(A(:,3)', q, 1)) ==
repmat(A(:,2)', q, 1))-1)*A(:,4)>0;

 figure(2);
 %scatter(Xc(:,1), Xc(:,2), 20, h, 'filled');
 clf;
 scatter(Xc(h>0,1), Xc(h>0,2), 20, 's', 'r');
 hold on;
 scatter(Xc(h<=0,1), Xc(h<=0,2), 20, 'o', 'b', 'filled');
 pause;

end;
