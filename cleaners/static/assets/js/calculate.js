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

        let cost=calculatePrice();

        $("#service_cost").val(cost);

        $("#main_form").submit();

    });

});