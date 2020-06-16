
var max_menu_width = parseInt($('.header_menu').css('max-width'));
var drop_list = $('div.drop_content > .drop_button');
var menu_list = $('div.header_menu > .header_button');

var header_menu = $('.header_menu')
var left_column = $('.left_column')
var header = $('.header');
var header_wrapper=$('.header_wrapper')
var search = $('.search')

var drop = $('div.header_drop').eq(0);
var max_menu_ele = drop_list.length + 2
var menu_ele_width = max_menu_width/max_menu_ele

function addEvents(){

    $('input[id=search_toggle]').change(function(){
        if($(this).is(':checked')) {
        search.hide()
        } else {
        search.show()
        }
    });

    $('input[id=header_toggle]').change(function(){
        if($(this).is(':checked')) {
        header_wrapper.hide()
        } else {
        header_wrapper.show()
        }
    });
    $('input[id=left_toggle]').change(function(){
        if($(this).is(':checked')) {
        left_column.hide()
        } else {
        left_column.show()
        }
    });
    resizeNavigation
}

function resizeNavigation(){
    var menu_width = $('.header_menu').width();
    
    for (elements = 2; elements < max_menu_ele; elements++){
        index = elements-2;
         
        if(menu_ele_width * (elements+1) < menu_width){
            drop_list.eq(index).hide()
            menu_list.eq(index).show()
        }else{
            drop_list.eq(index).show()
            menu_list.eq(index).hide()
        }
    }

    if(menu_width >= max_menu_width-menu_ele_width){
        drop.hide()
        menu_list.eq(max_menu_ele-3).show()
    }else{
        drop.show()
    }

    if($(window).width() <= 400){
        drop.hide()
        for (i = 0; i <max_menu_ele-2; i ++){
            menu_list.eq(i).show()
        }
    }

}

function header_accordion(){
    var header_menu = $('.header_menu');
    var header = $('.header');

    header.toggleClass("hidden");
    header_menu.toggleClass("hidden");
    /*
    console.log("klikki")
    if(header_menu.is(":hidden")){
      header_menu.show()
      header.show()
    }else{
      header_menu.hide()
      header.hide()
    }*/
    
  }

/*function header_accordion(){
    var header_menu = $('.header_menu');
    console.log("klikki")
    console.log(header_menu.is(":hidden"))
    if(header_menu.is(":hidden")){
      header_menu.show()
    }else{
      header_menu.hide()
    }
}*/

  var click = $('.header_max');
  click.bind("click",header_accordion);

$(document).ready(addEvents);
$(window).resize(resizeNavigation);
    //resizeNavigation);
