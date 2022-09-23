
$(".darkmode").click(function(){ //1
    $("body").toggleClass("dark")//2
      .css( //3
        $("body").hasClass("dark") ? //4
          {background:"#010508", color:"#f9f9f9"} : {background:"#f9f9f9", color:"#202225"} //5
      );

    $(".bg-white").toggleClass("dark")//2
      .css( //3
        $(".bg-white").hasClass("dark") ? //4
          {background:"#344258", color:"#f9f9f9"} : {background:"#f9f9f9", color:"#202225"} //5
      );

      $(".border-top").toggleClass("dark")//2
        .css( //3
          $(".border-top").hasClass("dark") ? //4
            {borderTop:"1px solid #000"} : {borderTop:"1px solid #eaebec"} //5
      );


  });
  

  
  // It's not clear if the ternary counts as 2 lines or 1 when I'm trying to minimise line count, but I'm counting it as 2
  