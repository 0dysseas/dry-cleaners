$(document).ready(function($) {

    "use strict";

    let calculatePrice = function() {

      let price;
      let types = {
        NRM: 25,
        SLK: 40,
        WOL: 15,
        PER: 20
      };

      let
          $carpet=$("#id_label_single"),
          $size=$("#meters"), //Caching jquery queries
          carpetType=$carpet.find('option:selected').val(),
          carpetMeters=$size.find('option:selected').val();

      if(carpetType !== null && carpetMeters !== null) {

          price=types[carpetType] + 10;

      }
      return price;
    };

    $("#calculate_btn").on('click',function(){
        $('.probootstrap-form').submit(false);

        let cost=calculatePrice();
        $("<div class='display-price'></div>").insertAfter( ".carpet-width" ); //TODO-me: Style this!
        $(".display-price").html(cost);

        $("#calculate_btn").val('Contact us!');

        $("#main_form").submit();

    });

});