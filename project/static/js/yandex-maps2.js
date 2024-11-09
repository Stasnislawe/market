ymaps.ready(init);

function init() {
    // Стоимость за километр.
    var DELIVERY_TARIFF = 15,
        // Минимальная стоимость.
        MINIMUM_COST = 200;
       window.myMap =  myMap = new ymaps.Map('map', {
            center: [60.906882, 30.067233],
            zoom: 9,
            controls: []
        });
        // Создадим панель маршрутизации.
        var routePanelControl = new ymaps.control.RoutePanel({ options: { // Добавим заголовок панели.
                showHeader: true,title: 'Расчёт доставки'}
            }),
        zoomControl = new ymaps.control.ZoomControl({ options: {size: 'small',float: 'none',position: { bottom: 145, right: 10 } } });
    // Пользователь сможет построить только автомобильный маршрут.
    routePanelControl.routePanel.options.set({ types: {auto: true} });

    // Если вы хотите задать неизменяемую точку "откуда", раскомментируйте код ниже.
    routePanelControl.routePanel.state.set({
        fromEnabled: false,
        from: [53.968149361067645, 58.40900849888758]
     });

        myMap.controls.add(routePanelControl);

    routePanelControl.routePanel.getRouteAsync().then(function (route) {

        route.model.setParams({results: 1}, true);

        route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();

            /*Ymaps.Events.observer(route, route.Events.Succes, function() {
                route.getWayPoint(0).setIconContent('Отправление');
                route.getWayPoint(1).setIconContent('Отправка');
            });*/

            if (activeRoute) {
                var length = route.getActiveRoute().properties.get("distance"),
                    points = route.getWayPoints(),
                    lastPoint = points.getLength() -1,
                    price = calculate(Math.round(length.value/ 1000)),

                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                        '<span style="font-weight: bold; font-style: italic">Стоимость доставки: ' + price + 'p.</span>');

                    route.options.set('routeBalloonContentLayout', balloonContentLayout);

                    document.getElementById('id_distance').value = length.text
                    document.getElementById('id_delivery_price').value = price
                    //document.getElementById('id_address').value = routePanelControl.routePanel.state.get('from')
                    //console.log(myMap.reverse(routePanelControl.routePanel.state.get('from')))

                    activeRoute.balloon.open();
                    var myCoordsto = routePanelControl.routePanel.state.get('to');
                    var myGeocoder = ymaps.geocode(myCoordsto);
                    myGeocoder.then(
                        function (res) {
                            var nearest = res.geoObjects.get(0);
                            var name = nearest.properties.get('text');
                            document.getElementById('id_address').value = name;
                        },
                        function (err) {
                            alert('Ошибка');
                        }
                    );
            }
        });
    });


    function calculate(routeLength) {
        return Math.max(routeLength * DELIVERY_TARIFF, MINIMUM_COST);
    }
}



