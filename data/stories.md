##story_for_wrong_input_user

* greet
    - action_greet
* inform
    - action_select_city
* inform
    - action_city
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform
    - action_category
    - action_city
* ask_reminder_category
    - action_category_reminder
* inform{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

##story_handle_fallbackaction_after_action_greet
* greet
    - action_greet
* inform
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"display reviews"}
    - action_opinion
* inform{"offers":"get more offers"}
    - slot{"offers":"get more offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}    
    - utter_goodbye
* goodbye

## New Story
* greet
    - action_greet
* inform
    - action_select_city
* inform
    - action_city
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform
    - action_category
    - action_city
* ask_reminder_category
    - action_category_reminder
* inform{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## story_004

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* ask_city_reminder
    - action_city_reminder
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* ask_reminder_category
    - action_category_reminder
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* ask_reminder_brand
    - action_brand_reminder
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand

## Story_00101_ask_category_after_deals
* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye
* goodbye

## Story_001011_ask_city_after_deals
* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye
    - export
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye
    - export

##story_006

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye
* goodbye    
* greet
    - action_greet
* inform
    - utter_ask_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye

##story_reminder_001

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* ask_reminder
    - action_set_reminder
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* ask_reminder
    - action_set_reminder
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye

## New Story_009

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye

## New Story

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## New Story_01011_normal

* greet
    - action_greet
* brand_deals{"brand_detail":"Brand deals?"}
    - slot{"brand_detail":"Brand deals?"}
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

##story_009

* greet
    - action_greet
* brand_deals{"brand_detail":"brand_details"}
    - slot{"brand_detail":"brand_details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand

##sstory_010

* greet
    - action_greet
* inform
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

##story_handle_action_city_method
* greet
    - action_greet
* inform
    - action_select_city
* inform
    - action_city
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## story_reminder_category
* greet
    - action_greet
* inform
    - action_select_city
* inform
    - action_city
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* ask_reminder_category
    - action_category_reminder
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## New Story_again_hi_with_agent

* greet
    - action_greet
* brand_deals{"brand_detail":"Brand deals?"}
    - slot{"brand_detail":"Brand deals?"}
    - action_select_city
* inform{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

##story_for_persistent_menu

* brand_deals{"brand_detail":"brand deals"}
    - slot{"brand_detail":"brand deals"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"Display Reviews"}
    - slot{"reviews":"Display Reviews"} 
    - action_opinion    
* inform{"offers":"Get More Offers"}
    - slot{"offers":"Get More Offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## New Story_for_normal

* greet
    - action_greet
* brand_deals{"brand_detail":"brand details"}
    - slot{"brand_detail":"brand details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
* inform{"offers":"get more offers"}
    - slot{"offers":"get more offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

##story_normal_user

* greet
    - action_greet
* inform
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"food & drinks"}
    - slot{"category_name":"food & drinks"}
    - action_category
* inform{"name":"pranzo"}
    - slot{"name":"pranzo"}
    - action_brand
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - action_email
    - utter_goodbye
* goodbye

##goodbye_after_display_Reviews

* greet
    - action_greet
* brand_deals{"brand_detail":"brand details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - action_brand
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
* goodbye
    - utter_goodbye

##story_for_normal

* greet
    - action_greet
* brand_deals{"brand_detail":"brand details"}
    - slot{"brand_detail":"brand details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
* inform{"offers":"get more offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye

## bye after asking brand

* greet
    - action_greet
* brand_deals{"brand_detail":"brand details"}
    - slot{"brand_detail":"brand details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
* goodbye
    - utter_goodbye
* goodbye

## bye after email
* greet
    - action_greet
    - slot{"brand_detail":"brand details"}
* brand_deals{"brand_detail":"brand details"}
    - action_select_city
    - slot{"city_name":"karachi"}
* inform{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
    - slot{"category_name":"lifestyle"}
* inform{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"orchard.pk"}
    - slot{"name":"orchard.pk"}
    - action_brand
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
    - slot{"offers":"get more offers"}
* inform{"offers":"get more offers"}
    - action_email
* goodbye
    - utter_goodbye
* goodbye

## New Story

* greet
    - action_greet
* brand_deals{"brand_detail":"brand details"}
    - slot{"brand_detail":"brand details"}
    - action_select_city
* inform{"city_name":"karachi"}
    - slot{"city_name":"karachi"}
    - action_city
    - slot{"city_name":"karachi"}
* inform{"category_name":"lifestyle"}
    - slot{"category_name":"lifestyle"}
    - action_category
    - slot{"category_name":"lifestyle"}
* inform{"name":"asdjqwe"}
    - slot{"name":"asdjqwe"}
    - action_brand
    - slot{"name":"asdjqwe"}
    - slot{"city_name":"karachi"}
    - slot{"category_name":"lifestyle"}
* inform{"name":"ego"}
    - slot{"name":"ego"}
    - action_brand
    - slot{"name":"ego"}
    - slot{"city_name":"karachi"}
    - slot{"category_name":"lifestyle"}
* inform{"reviews":"display reviews"}
    - slot{"reviews":"display reviews"}
    - action_opinion
* inform{"offers":"get more offers"}
    - slot{"offers":"get more offers"}
    - action_email
* inform{"email":"attitudebreaker17@gmail.com"}
    - slot{"email":"attitudebreaker17@gmail.com"}
    - utter_goodbye
* goodbye
