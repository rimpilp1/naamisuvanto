
var max_menu_width = parseInt($('.header_menu').css('max-width'));
var drop_list = $('div.drop_content > .drop_button');
var menu_list = $('div.header_menu > .header_button');
var drop = $('div.header_drop').eq(0);
var max_menu_ele = drop_list.length + 2
var menu_ele_width = max_menu_width/max_menu_ele

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

    if($(window).width() < 400){
        drop.hide()
        for (i = 0; i <max_menu_ele-2; i ++){
            menu_list.eq(i).show()
        }
    }

}

$(document).ready(resizeNavigation);
$(window).resize(resizeNavigation);
