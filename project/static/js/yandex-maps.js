/*ymaps.ready(init);
function init(){
    var DELIVERY_TARIFF = 16,
        MINIMUM_COST = 200,
        myMap = new ymaps.Map("map", {
            center: [53.96, 58.41],
            zoom: 14,
            controls: []
    });

        routePanelControl = new ymaps.control.RoutePanel({
            options: {
                showHeader: true,
                titile: 'Расчёт доставки'
            }
        }),
        zoomControl = new ymaps.control.ZoomControl({
            options: {
                size: 'small',
                float: 'none',
                position: {
                    bottom: 145,
                    right: 10
                }
            }
        });

    routePanelControl.routePanel.options.set({
        types: {auto: true}
    });

    routePanelControl.routePanel.state.set({
        fromEnabled: false,
        from: 'Белорецк улица Карла Маркса 70А'
    });


    myMap.controls.add(routePanelControl).add(zoomControl);

    routePanelControl.routePanel.getRouteAsync().then(function (route) {

        route.model.setParams({results: 1}, true);

        route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();



            if (activeRoute) {
                var length = route.getActiveRoute().properties.get("distance"),
                    price = calculate(Math.round(length.value/ 1000)),

                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                        '<span style="font-weight: bold; font-style: italic">Стоимость доставки: ' + price + 'p.</span>');

                    route.options.set('routeBalloonContentLayout', balloonContentLayout);

                    document.getElementById('distance_id').value = length.text
                    document.getElementById('oplata_id').value = price
                    document.getElementById('id_address').value = route.geoObject.properties
                    activeRoute.balloon.open();

            }
        });
    });

    function calculate(routeLength) {
        return Math.max(routeLength * DELIVERY_TARIFF, MINIMUM_COST);
    }
}*/

ymaps.ready(init);

function init() {
    var DELIVERY_TARIFF = 16,
        MINIMUM_COST = 200,
        myPlacemark,
        StaticPlacemark,
        myMap = new ymaps.Map('map', {
            center: [53.96, 58.41],
            zoom: 14
        });

    var StaticPlacemark = new ymaps.Placemark([53.968149361067645, 58.40900849888758], null, {
        preset: 'islands#blueDotIcon'
    });

    myMap.geoObjects.add(StaticPlacemark);

    // Слушаем клик на карте.
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');

        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
            myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
            myPlacemark = createPlacemark(coords);
            myMap.geoObjects.add(myPlacemark);
            // Слушаем событие окончания перетаскивания на метке.
            myPlacemark.events.add('dragend', function () {
                getAddress(myPlacemark.geometry.getCoordinates());
            });
        }
        getAddress(coords);
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {
            iconCaption: 'поиск...'
        }, {
            preset: 'islands#violetDotIconWithCaption',
            draggable: true
        });
    }

    // Определяем адрес по координатам (обратное геокодирование).
    function getAddress(coords) {
        myPlacemark.properties.set('iconCaption', 'поиск...');
        ymaps.geocode(coords).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);

            myPlacemark.properties
                .set({
                    // Формируем строку с данными об объекте.
                    iconCaption: [
                        // Название населенного пункта или вышестоящее административно-территориальное образование.
                        firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                        // Получаем путь до топонима, если метод вернул null, запрашиваем наименование здания.
                        firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                    ].filter(Boolean).join(', '),
                    // В качестве контента балуна задаем строку с адресом объекта.
                    balloonContent: firstGeoObject.getAddressLine()
                });
                document.getElementById('id_address').value = firstGeoObject.getAddressLine();
        });
    }

    ymaps.route([StaticPlacemark, myPlacemark]).then(
        function(route) {
            var distance = route.getHumanLength();
            document.getElementById('distance_id').value = distance.text
            myMap.geoObjects.add(route)
        }
    );

    /*myMap.controls.add(routePanelControl);

    routePanelControl.routePanel.getRouteAsync().then(function (route) {

        route.model.setParams({results: 1}, true);

        route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();



            if (activeRoute) {
                var length = route.getActiveRoute().properties.get("distance"),
                    price = calculate(Math.round(length.value/ 1000)),

                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                        '<span style="font-weight: bold; font-style: italic">Стоимость доставки: ' + price + 'p.</span>');

                    route.options.set('routeBalloonContentLayout', balloonContentLayout);

                    document.getElementById('distance_id').value = length.text
                    document.getElementById('oplata_id').value = price
                    activeRoute.balloon.open();

            }
        });
    });

    function calculate(routeLength) {
        return Math.max(routeLength * DELIVERY_TARIFF, MINIMUM_COST);
    }*/

    /*var multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [
            StaticPlacemark,
            myPlacemark
        ],
        params: {
            routingMode: "auto"
        }
    }, {
        boundsAutoApply: true
    });

    myMap.geoObjects.add(MultiRoute);

    var distance = multiRoute.getActiveRoute().properties.get("distance")
        let distance_km = Math.round(distance.value/ 1000)

    document.getElementById('distance_id').value = distance.text;*/

    /*routePanelControl.routePanel.state.set({
        from: StaticPlacemark,
        to: myPlacemark
    });

    myMap.controls.add(routePanelControl);

    routePanelControl.routePanel.getRouteAsync().then(function (route) {

        route.model.setParams({results: 1}, true);

        route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();



            if (activeRoute) {
                var length = route.getActiveRoute().properties.get("distance"),
                    price = calculate(Math.round(length.value/ 1000)),

                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                        '<span style="font-weight: bold; font-style: italic">Стоимость доставки: ' + price + 'p.</span>');

                    route.options.set('routeBalloonContentLayout', balloonContentLayout);

                    document.getElementById('distance_id').value = length.text
                    document.getElementById('oplata_id').value = price
                    activeRoute.balloon.open();

            }
        });
    });


    function calculate(routeLength) {
        return Math.max(routeLength * DELIVERY_TARIFF, MINIMUM_COST);
    }*/
}