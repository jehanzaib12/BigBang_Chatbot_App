from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
from datetime import datetime, timedelta

import requests
import os
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from itertools import islice
import re
from rasa_sdk.events import ReminderScheduled, ReminderCancelled, FollowupAction



# key 8c96f578e5b37e9083158c1f6eb8bf57


class Actiongreet(Action):

    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):

        try:

            #id = tracker.sender_id
            print("getting id")
            id = 4687187787965563
            id = int(id)
            print(type(id))
            userid = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token=EAAI2m1iiQisBAHLRL2d4QZBgt3jSvJXZBDIqGZA8jHfStjYXh3G2VagFqL5AIdcRYTMIqvlV9TRky68DEXlz3DsSFL4VZBIt7G9WJV0o3jqCfGW95TXAvh3qyZBm66Nb1gLHzIBX8ZCaLUXx6o2aSOjUsCfLljUhYpZBcZBtXXjsvQZDZD".format(
                    id)).json()
            print(userid)
            print("getting userid")

            # get started button
            get_started = {
                "get_started": {
                    "payload": "GET STARTED"
                }
            }
            print(get_started)
            headers = {'content-type': 'application/json'}

            url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAI2m1iiQisBAHLRL2d4QZBgt3jSvJXZBDIqGZA8jHfStjYXh3G2VagFqL5AIdcRYTMIqvlV9TRky68DEXlz3DsSFL4VZBIt7G9WJV0o3jqCfGW95TXAvh3qyZBm66Nb1gLHzIBX8ZCaLUXx6o2aSOjUsCfLljUhYpZBcZBtXXjsvQZDZD"

            requests.post(url=url, data=json.dumps(get_started), headers=headers)

            menu = {
                "psid": id,
                "persistent_menu": [
                    {
                        "locale": "default",
                        "composer_input_disabled": False,
                        "call_to_actions": [
                            {
                                "type": "postback",
                                "title": "Brand deals?",
                                "payload": "Brand deals?"
                            },
                            {
                                "type": "web_url",
                                "title": "Shop now",
                                "url": "https://www.bigbang.pk/",
                                "webview_height_ratio": "tall"
                            }
                        ]
                    }
                ]
            }
            headers = {'content-type': 'application/json'}
            # dispatcher.utter_custom_json(menu)
            print(menu)

            url = "https://graph.facebook.com/v6.0/me/custom_user_settings?access_token=EAAI2m1iiQisBAHLRL2d4QZBgt3jSvJXZBDIqGZA8jHfStjYXh3G2VagFqL5AIdcRYTMIqvlV9TRky68DEXlz3DsSFL4VZBIt7G9WJV0o3jqCfGW95TXAvh3qyZBm66Nb1gLHzIBX8ZCaLUXx6o2aSOjUsCfLljUhYpZBcZBtXXjsvQZDZD"

            requests.post(url=url, data=json.dumps(menu), headers=headers)

            # sender action by me

            body = {
                "recipient": {
                    "id": id
                },
                "sender_action": "typing_on"
            }
            print(body)
            headers = {'content-type': 'application/json'}
            url = "https://graph.facebook.com/v5.0/me/messages?access_token=EAAI2m1iiQisBAHLRL2d4QZBgt3jSvJXZBDIqGZA8jHfStjYXh3G2VagFqL5AIdcRYTMIqvlV9TRky68DEXlz3DsSFL4VZBIt7G9WJV0o3jqCfGW95TXAvh3qyZBm66Nb1gLHzIBX8ZCaLUXx6o2aSOjUsCfLljUhYpZBcZBtXXjsvQZDZD"

            requests.post(url=url, data=json.dumps(body), headers=headers)


            fn = ""
            for key, value in userid.items():
                fn = value
                print(fn)
                break

            res1 = {
                "text": "Welcome to BigBang Discount Assistant {}. Get started by clicking the button given below\n For Customer Support, you can join this link to talk to our Customer Representative\n m.me/arsalan.virgo".format(fn),

                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Brand details",
                        "payload": "Brand details"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)
        except:
            dispatcher.utter_message("BigBang Chatbot Didnt recognize the text!")
            return [FollowupAction("action_greet")]

class ActionSelectCity(Action):
    def name(self):
        return 'action_select_city'

    def run(self, dispatcher, tracker, domain):
        try:
            city = {

                "text": "Select your city from the list below:",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Karachi",
                        "payload": "Karachi"
                    },
                    {
                        "content_type": "text",
                        "title": "Lahore",
                        "payload": "Lahore"
                    },
                    {
                        "content_type": "text",
                        "title": "Islamabad",
                        "payload": "Islamabad"
                    },
                    {
                        "content_type": "text",
                        "title": "Faisalabad",
                        "payload": "Faisalabad"
                    },
                    {
                        "content_type": "text",
                        "title": "Sanghar",
                        "payload": "Sanghar"
                    }
                ]
            }

            dispatcher.utter_custom_json(city)
            print(city)
            return [ReminderScheduled("ask_city_reminder", datetime.now() + timedelta(seconds=300))]
        except:
            dispatcher.utter_message("BigBang Didnt recognize the text! Try Again!")
            return [FollowupAction("action_select_city")]

class ActionCity(Action):
    city_key = 0

    def name(self):
        return 'action_city'

    def run(self, dispatcher, tracker, domain):

        try:
            city_response = "http://165.227.69.207:9001/api/country/get"
            city_response_json = requests.get(city_response).json()
            print(city_response_json)

            print("--------cityid--------------------")
            city_namee = tracker.get_slot('city_name')

            if city_namee == None:
                print("city not coming")

            else:
                print("city coming " + city_namee)

            city_res = ""
            city_ls = {}
            cityls = []

            for i in city_response_json["data"][0]["cities"]:
                city_id = i["_id"]
                city_name = i["city_name"]
                city_ls.update({city_name: city_id})
                cityls.append(city_name)

            print(city_namee)
            city_ls = {k.lower(): v for k, v in city_ls.items()}

            for key, value in city_ls.items():
                if city_namee in key:
                    print(city_namee)
                    print(key, value)

            cn = '\\w*'.join(city_namee) + '\\w*'
            print("user input" + cn)

            city__ls = '\n'.join(cityls)
            print(city__ls)
            city_re = re.findall(r'{}'.format(cn), city__ls.lower())
            print(city_re)

            city_re = '\n'.join(city_re)
            print(city_re)

            if city_re in city_ls:
                print(city_namee)
                # response = "Select Any One Category: \n" + "1. Food & Drinks\n" + "2. Lifestyle\n" \
                # 		   + "3. Beauty & Fitness\n" + "4. Entertainment\n" + \
                # 		   "5. Healthcare\n" + "6. Education\n" + "7. Services\n"
                # print(response)

                category = {

                    "text": "Tell me the category to show you the related brands? ",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "Food & Drinks",
                            "payload": "Food & Drinks"
                        },
                        {
                            "content_type": "text",
                            "title": "Lifestyle",
                            "payload": "Lifestyle"

                        },
                        {
                            "content_type": "text",
                            "title": "Beauty & Fitness",
                            "payload": "Beauty & Fitness"

                        },
                        {
                            "content_type": "text",
                            "title": "Entertainment",
                            "payload": "Entertainment"

                        },
                        {
                            "content_type": "text",
                            "title": "Healthcare",
                            "payload": "Healthcare"

                        },
                        {
                            "content_type": "text",
                            "title": "Education",
                            "payload": "Education"

                        },
                        {
                            "content_type": "text",
                            "title": "Services",
                            "payload": "Services"

                        }
                    ]
                }

                dispatcher.utter_custom_json(category)
                print(category)
                print(category)
            else:
                iterator = islice(cityls, 7)
                nf = "The city doesn't exists. Please Check Spelling Error and Re-Type city from Below List:\n" + "\n".join(
                    iterator)
                dispatcher.utter_message(nf)

            return [SlotSet('city_name', city_namee),
                    ReminderScheduled("ask_reminder_category", datetime.now() + timedelta(seconds=300))]
        except:
            dispatcher.utter_message("BigBang Didnt recognize the text! Try Again!")
            return [FollowupAction("action_select_city")]


class ActionReactToReminder(Action):
    # cat_key = 1
    def name(self):
        return 'action_category_reminder'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("BigBang ChatBot is waiting for your reply")
        category = {

            "text": "Tell me the category to show you the related brands? ",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Food & Drinks",
                    "payload": "Food & Drinks"
                },
                {
                    "content_type": "text",
                    "title": "Lifestyle",
                    "payload": "Lifestyle"

                },
                {
                    "content_type": "text",
                    "title": "Beauty & Fitness",
                    "payload": "Beauty & Fitness"

                },
                {
                    "content_type": "text",
                    "title": "Entertainment",
                    "payload": "Entertainment"

                },
                {
                    "content_type": "text",
                    "title": "Healthcare",
                    "payload": "Healthcare"

                },
                {
                    "content_type": "text",
                    "title": "Education",
                    "payload": "Education"

                },
                {
                    "content_type": "text",
                    "title": "Services",
                    "payload": "Services"

                }
            ]
        }

        dispatcher.utter_custom_json(category)

        return []


class ActionReactToReminder(Action):
    # cat_key = 1
    def name(self):
        return 'action_brand_reminder'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "BigBang ChatBot is waiting for your reply, Please select the brand from the above list")


class ActionReactToReminder(Action):
    # cat_key = 1
    def name(self):
        return 'action_city_reminder'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("BigBang ChatBot is waiting for your reply")
        city = {

            "text": "Select your city from the list below:",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Karachi",
                    "payload": "Karachi"
                },
                {
                    "content_type": "text",
                    "title": "Lahore",
                    "payload": "Lahore"
                },
                {
                    "content_type": "text",
                    "title": "Islamabad",
                    "payload": "Islamabad"
                },
                {
                    "content_type": "text",
                    "title": "Faisalabad",
                    "payload": "Faisalabad"
                },
                {
                    "content_type": "text",
                    "title": "Sanghar",
                    "payload": "Sanghar"
                }
            ]
        }

        dispatcher.utter_custom_json(city)
        return []


class ActionCategory(Action):
    # cat_key = 1

    def name(self):
        return 'action_category'

    def run(self, dispatcher, tracker, domain):

        try:
            category_response = "http://165.227.69.207:9001/api/category/get"
            category_response_json = requests.get(category_response).json()
            category_ls = {}
            categoryls = []

            c_name = tracker.get_slot('category_name')

            if c_name == None:
                print("category not coming")
            else:
                print("category coming" + c_name)
            # category_input = str(input("Enter Category Name"))
            for i in category_response_json["data"]:
                category_id = i["_id"]
                category_name = i["name"]
                category_ls.update({category_name: category_id})
                categoryls.append(category_name)

            category_ls = {k.lower(): v for k, v in category_ls.items()}

            # return cat_key

            category = '\\w*'.join(c_name) + '\\w*'
            print(category)
            categoryls = '\n'.join(categoryls)
            cat_re = re.findall(r'{}'.format(category), categoryls.lower())
            print(cat_re)
            cat_re = '\n'.join(cat_re)

            for key, value in category_ls.items():
                if cat_re in key:
                    print(key, value)
                    cat_key = value

            if cat_re in category_ls:
                print(c_name)
                # c_name = c_name.toUpper()
                response = "Select Your Favourite {} brand from below list".format(c_name)
                print(response)

                city_response = "http://165.227.69.207:9001/api/country/get"
                city_response_json = requests.get(city_response).json()
                print("-getting city name")
                city_namee = tracker.get_slot('city_name')

                if city_namee == None:
                    print("city not coming")

                else:
                    print("city coming " + city_namee)

                    city_ls = {}
                    cityls = []
                    print("coming here")
                    for i in city_response_json["data"][0]["cities"]:
                        city_id = i["_id"]
                        city_name = i["city_name"]
                        city_ls.update({city_name: city_id})
                        cityls.append(city_name)

                    print("getting re")
                    cn = '\\w*'.join(city_namee) + '\\w*'
                    print(cn)

                    cityls = '\n'.join(cityls)
                    print(cityls)
                    city_re = re.findall(r'{}'.format(cn), cityls.lower())
                    city_re = '\n'.join(city_re)
                    print("city name after taking out from list" + city_re)

                    print(city_namee)

                    city_ls = {k.lower(): v for k, v in city_ls.items()}
                    for key, value in city_ls.items():
                        if city_re in key:
                            print(city_re)
                            print(key, value)
                            city_key = value

                            print(cat_key)
                            print(city_key)
                            brand_response = "http://165.227.69.207:9001/api/category/getBrandCategoryPagination/{}?page=1&limit=10&city_id={}".format(
                                cat_key, city_key)
                            brand_response_json = requests.get(brand_response).json()
                            print("brand list coming")
                            brand_ls = []

                    brand_lss = []
                    if brand_response_json['message'] != 'No category found':
                        count1 = 1
                        gt = {}
                        for i in brand_response_json["data"][0]["result"]:
                            brand_name = "{}. ".format(count1) + i["name"]
                            count1 = count1 + 1
                            bn = i["name"]
                            brand_ls.append(brand_name)
                            brand_lss.append(bn)

                        for i in brand_ls:
                            print(i)
                        iterator = islice(brand_ls, 10)

                        output = "Select the brand from the top brands:\n" + '\n'.join(iterator)

                        dispatcher.utter_message(output)
                        print(output)

                    else:
                        print("There is no brand found in: {} category".format(c_name))
                        notfound = "There is no brand found in: {} category".format(c_name)
                        dispatcher.utter_message(notfound)

            else:
                iterator = islice(categoryls, 7)
                nf = "The category doesn't exists. Please Check Spelling Error and Re-Type Category from Below List:\n" + "\n".join(
                    iterator)
                dispatcher.utter_message(nf)
                print(nf)

            return [SlotSet('category_name', c_name),
                    ReminderScheduled("ask_reminder_brand", datetime.now() + timedelta(seconds=300))]

        except:
            dispatcher.utter_message('BigBang Didnt recognize the text! Try Again!')
            return [FollowupAction("action_city")]


class ActionWeather(Action):
    def name(self):
        return 'action_brand'

    def run(self, dispatcher, tracker, domain):

        import requests
        try:
            city_response = "http://165.227.69.207:9001/api/country/get"
            city_response_json = requests.get(city_response).json()

            category_response = "http://165.227.69.207:9001/api/category/get"
            category_response_json = requests.get(category_response).json()

            print("-getting city name")
            city_namee = tracker.get_slot('city_name')

            if city_namee == None:
                print("city not coming")

            else:
                print("city coming " + city_namee)

                city_ls = {}
                cityls = []

                for i in city_response_json["data"][0]["cities"]:
                    city_id = i["_id"]
                    city_name = i["city_name"]
                    city_ls.update({city_name: city_id})
                    cityls.append(city_name)

                cn = '\\w*'.join(city_namee) + '\\w*'
                print(cn)

                cityls = '\n'.join(cityls)
                print(cityls)
                city_re = re.findall(r'{}'.format(cn), cityls.lower())
                city_re = '\n'.join(city_re)

                print(city_namee)
                city_ls = {k.lower(): v for k, v in city_ls.items()}
                for key, value in city_ls.items():
                    if city_re in key:
                        print(city_namee)
                        print(key, value)
                        city_key = value

            print("getting category name")
            c_name = tracker.get_slot('category_name')

            if c_name == None:
                print("category not coming")
            else:
                print("category coming" + c_name)

            category_ls = {}
            categoryls = []

            for i in category_response_json["data"]:
                category_id = i["_id"]
                category_name = i["name"]
                category_ls.update({category_name: category_id})
                categoryls.append(category_name)

            category_ls = {k.lower(): v for k, v in category_ls.items()}
            category = '\\w*'.join(c_name) + '\\w*'
            categoryls = '\n'.join(categoryls)
            cat_re = re.findall(r'{}'.format(category), categoryls.lower())
            print(cat_re)
            cat_re = '\n'.join(cat_re)

            for key, value in category_ls.items():
                if cat_re in key:
                    print(key, value)
                    cat_key = value

            brand_response = "http://165.227.69.207:9001/api/category/getBrandCategoryPagination/{}?page=1&limit=10&city_id={}".format(
                cat_key, city_key)
            # brand_response = "http://165.227.69.207:9001/api/category/getBrandByCategory/53616c7465645f5f9704cc2abbca7736a2bcf703f02d0ae122204eadd80af9d879de83e69568ccfcd4f28b2fb8ccbbf9?city_id=5d6fafacdd5a444cf6925cf2&customer_id=53616c7465645f5faa59ae365d53a918300db538b645f77228ee71e304203c78dd7d9ef7916465f50aebc40159a6d677"
            brand_response_json = requests.get(brand_response).json()

            print(brand_response)
            print("getting brand name")

            loc = tracker.get_slot('name')
            if loc == None:
                print("brand name not coming")
            else:
                print("brand name coming" + loc)

            loc = loc.lower()

            brand_ls = []
            brand_re = []
            for i in brand_response_json["data"][0]["result"]:
                brand_name = i["name"]
                brand_ls.append(brand_name)
                brand_re.append(brand_name)

            bn = '\\w*'.join(loc) + '\\w*'
            brand_re = '\n'.join(brand_re)
            brand_re = re.findall(r'{}'.format(bn), brand_re.lower())
            brand_re = '\n'.join(brand_re)
            print("converting list into name" + brand_re)

            list_of_deals = []
            brand_lst = [x.lower() for x in brand_ls]
            deal_lss = []
            ls = []

            if brand_lst.__contains__(brand_re):
                print("brand exists" + brand_re)
                count = 1
                print("{} deals & offers: ".format(brand_re))
                response_brand_name = "{} deals & offers: ".format(brand_re)

                response_list = "Here are the list of deals: "
                dispatcher.utter_message(response_list)

                for i in brand_response_json["data"][0]["result"]:
                    for j in i["offer"]:
                        if brand_re.upper() == i["name"].upper():
                            title = j["title"]
                            sub_title = j["sub_title"]
                            offer_description = j["offer_description"]
                            # star = "------------------------------------------------------"

                            print("DEAL: " + title)
                            response_title = "**DEAL {}: **".format(count)
                            count = count + 1
                            list_of_deals.append(response_title)
                            title = "Name: " + title
                            list_of_deals.append(title)
                            if sub_title == "":
                                print(end='')
                                response_sub_title = end = ''
                            else:
                                print("Offer on this deal is: " + sub_title)
                                response_sub_title = "OFFER: " + sub_title
                                list_of_deals.append(response_sub_title)
                            print("Offer description on this deal is: " + offer_description)
                            response_offer_description = "OFFER DESCRIPTION: " + offer_description
                            list_of_deals.append(response_offer_description)
                            off = "      **Next Deal**      "
                            imgurl = i["icon"]

                            ls1 = {
                                "title": title,
                                "image_url": "http://165.227.69.207:9001/{}".format(imgurl),
                                "subtitle": sub_title,
                                   "buttons": [
                                       {
                                        "type": "web_url",
                                        "url": "https://www.bigbang.pk/",
                                        "title": "View BigBang Website",
                                        "webview_height_ratio": "tall"
                                       }
                                   ]
                                }


                            ls.append(ls1)
                            print(ls)
                            print("list")

                gt = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": ls

                        }
                    }
                }
                dispatcher.utter_custom_json(gt)
                print(gt)




                res_admin = {

                    "text": "Do you want to ask more? ",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "display reviews",
                            "payload": "Display Reviews"

                        },
                        {
                            "content_type": "text",
                            "title": "No, thankyou",
                            "payload": "No, thankyou"

                        }
                    ]
                }

                dispatcher.utter_custom_json(res_admin)
                print(res_admin)

                print(list_of_deals)
                print("Thankyou, Want to ask more?")
                iterator = islice(list_of_deals, 6)
                deals_output = "Here are the top deals & offers:\n" + '\n'.join(iterator)

                print("Inside custom action payload")

                # dispatcher.utter_message(template="utter_test_custom_output")

                # dispatcher.utter_message(deals_output)
                print(deals_output)
            else:
                print("brand not found")
                print(brand_ls)
                iterate = islice(brand_ls, 35)
                nf = "Brand Not Found. Please Check Your Spelling & Retype Brand Name Again from below List:\n" + '\n'.join(
                    iterate)
                dispatcher.utter_message(nf)
                print(nf)

            # print(deals_output)

            # print(loc)
            return [SlotSet('name', loc), SlotSet('city_name', city_namee), SlotSet('category_name', c_name)]
        except:
            dispatcher.utter_message("BigBang Didnt recognize the text! Try Again!")
            return [FollowupAction("action_brand")]

# method to send primary receiver to secondary receiver

# class Actioncalladmin(Action):
#     # cat_key = 1
#     def name(self):
#         return 'action_call_admin'
#
#     def run(self, dispatcher, tracker, domain):
#
#         try:
#            # id = int(tracker.sender_id)
#             id = 2844229312359076
#             print("before pass thread control")
#             hjj1 = requests.get(
#                 "https://graph.facebook.com/v2.6/me/thread_owner?recipient={}&access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD".format(id)).json()
#             print(hjj1)
#
#
#
#             # passing thread owner to page inbox or secondary receiver
#             body = {
#                 "recipient": {
#                     "id": id,
#                 },
#                 "target_app_id": 263902037430900,
#                 "metadata": "String to pass to secondary receiver app",
#             }
#             print(body)
#             headers = {'content-type': 'application/json'}
#             url = "https://graph.facebook.com/v2.6/me/pass_thread_control?access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD"
#
#             hj = requests.post(url=url, data=json.dumps(body), headers=headers)
#             if hj.status_code != 200:
#                 print(hj.status_code)
#                 print(hj.text)
#             else:
#                 print("HANDOVER THREAD CONTROL")
#
#             # setting up persona for secondary user
#             persona = {
#                 "name": "Jehanzaib",
#                 "profile_picture_url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=2844229312359076&width=1024&ext=1590643301&hash=AeSgPJJf76FlRs2O"
#             }
#             print(persona)
#             url1 = "https://graph.facebook.com/me/personas?access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD"
#
#             hjj = requests.post(url=url1, data=json.dumps(persona), headers=headers)
#             if hjj.status_code != 200:
#                 print(hjj.status_code)
#                 print(hjj.text)
#             else:
#                 print("HANDOVER PERSONA ID")
#
#             # sending messages as persona
#             persona_send = {
#                 "recipient": {
#                     "id": id
#                 },
#                 "message": {
#                     "text": "Hello from jehanzaib Agent from BigBang ChatBot, How Can I Help You?",
#                 },
#                 "persona_id": 959900441092769
#             }
#             print(persona_send)
#             url2 = "https://graph.facebook.com/me/messages?access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD"
#             requests.post(url=url2, data=json.dumps(persona_send), headers=headers)
#
#             # # getting the persona details
#             # print("getting persona details")
#             # requests.get(
#             #     "https://graph.facebook.com/703275023743834?access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD")
#
#             # getting the thread owner app id
#             app_id = requests.get(
#                 "https://graph.facebook.com/v2.6/me/thread_owner?recipient={}&access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD".format(id)).json()
#             print(app_id)
#
#             # passing the thread owner back to the primary receiver
#             while (True):
#                 # print("after making done")
#                 app_id = requests.get(
#                     "https://graph.facebook.com/v2.6/me/thread_owner?recipient={}&access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD".format(id)).json()
#                 print(app_id["data"][0]["thread_owner"]["app_id"])
#
#                 if (int)(app_id["data"][0]["thread_owner"]["app_id"]) == 627531511140634:
#                     # FollowupAction("action_goodbye")
#                     print("secondary receiver has given the handover to primary receiver")
#                     break
#             print("successfully passed")
#             dispatcher.utter_template("utter_goodbye",tracker)
#         except:
#             dispatcher.utter_message("BigBang Didnt recognize the text! Try Again! admin")
#             print("BigBang Didnt recognize the text! Try Again! admin")
            #return [FollowupAction("action_greet")]


# if hj.status_code != 200:
# 	print(hj.status_code)
# 	print(hj.text)
# else:
# 	print("HANDOVER")


# dispatcher.utter_custom_json(passData)


# dispatcher.utter_custom_json(passData)


class Actionopinion(Action):
    def name(self):
        return 'action_opinion'

    def run(self, dispatcher, tracker, domain):

        try:
            res = {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "media",
                        "elements": [
                            {
                                "media_type": "video",
                                "url": "https://www.facebook.com/bigbangapp/videos/2779235688797355/",
                            }
                        ]
                    }
                }
            }
            # }
            dispatcher.utter_custom_json(res)
            print(res)

            res1 = {

                "text": "Any more questions? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Get More Offers",
                        "payload": "<POSTBACK_PAYLOAD>",

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "<POSTBACK_PAYLOAD>",

                    }
                ]
            }

            dispatcher.utter_custom_json(res1)
        except:
            dispatcher.utter_message("BigBang Didnt recognize the text! Try Again!")
            return [FollowupAction("action_opinion")]

class ActionLocation(Action):
    def name(self):
        return 'action_email'

    def run(self, dispatcher, tracker, domain):

        try:
            response = {
                "text": 'Send us your email to get more deals and offers. Subscribe by clicking the button of your email below',
                "quick_replies": [
                    {
                        "content_type": "user_email"
                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"
                    }

                ]
            }

            print(response)
            dispatcher.utter_custom_json(response)
            return []
        except:
            dispatcher.utter_message("BigBang Didnt recognize the text! Try Again!")
            return [FollowupAction("action_email")]

class ActionLocation(Action):
    def name(self):
        return 'action_goodbye'

    def run(self, dispatcher, tracker, domain):
        response = "Its being nice to talk to you, Bye Bye :)"
        dispatcher.utter_message(response)
        print(response)
        return []


# class Actionfallback(Action):
#     def name(self):
#         return 'action_fallback'
#
#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message("Bigbang chatbot doesn't recognize the text! fallback")
#         print("Bigbang chatbot doesn't recognize the text! fallback ")
#
#         return [FollowupAction("action_greet")]

# the method to call the representative

# class ActionLocation(Action):
# 	def name(self):
# 		return 'action_representative'
#
# 	def run(self, dispatcher, tracker, domain):
#
# 		# response = {
# 		# 		"attachment":{
# 		# 		  "type":"template",
# 		# 		  "payload":{
# 		# 			"template_type":"button",
# 		# 			"text":"Need further assistance? Talk to a BigBang representative on our helpline number",
# 		# 			"buttons":[
# 		# 			  {
# 		# 				"type":"phone_number",
# 		# 				"title":"Call Representative",
# 		# 				"payload":"+15105551234"
# 		# 			  },
# 		# 				{
# 		# 					"type": "text",
# 		# 					"title": "No, Thankyou",
# 		# 					"payload": "No, Thankyou"
# 		# 				}
# 		# 			]
# headers = {'content-type': 'application/json'}
# url = "https://graph.facebook.com/v6.0/me/messages?access_token=EAAI6vJDOkRoBAOX8H3k6yjxCev2RrN9XRM6pnqzYP4Ez8vcZAt4MrB877kpUWdRqyJbj8OJ6W9lHNn9leDu1x1gWw9Cy298JWeXfqsZCcPqdqkLsrSaEWm9BFysFfKttJsmLDWm0c5QIZBldHE7X3IkcZApXxKRkZC5dDRCEsKgZDZD"
# hj = requests.post(url=url, data=json.dumps(response), headers=headers)
#
# if hj.status_code != 200:
# 	print(hj.status_code)
# 	print(hj.text)
# else:
# 	print("HANDOVER")



# the method of one_time_notification for further use

# class Actionnotication(Action):
# 	def name(self):
# 		return 'action_notification'
#
# 	def run(self, dispatcher, tracker, domain):
# 		message = "Unfortunately, this item isnt in the stock at this moment, but we can let you know when it will come"
# 		dispatcher.utter_message(message)
# 		print(message)
#
# 		res = {
# 				"attachment": {
# 					"type": "template",
# 					"payload": {
# 						"template_type": "one_time_notif_req",
# 						"title": "Notify Me",
# 						"payload": "Notify Me"
# 					}
# 				}
# 			}
#
# 		dispatcher.utter_custom_json(res)
# 		print(res)

# class Actionqrcode(Action):
# 	def name(self):
# 		return 'action_qrcode'
#
# 	def run(self, dispatcher, tracker, domain):

# receipt method for further use

# class Actionreceipt(Action):
# 	def name(self):
# 		return 'action_receipt'
#
# 	def run(self, dispatcher, tracker, domain):
#
# 		message = "This is the recipient that you order"
# 		dispatcher.utter_message(message)
# 		print(message)
#
# 		res = {
# 				"attachment": {
# 					"type":"template",
# 					  "payload":{
# 						"template_type":"receipt",
# 						"recipient_name":"Stephane Crozatier",
# 						"order_number":"12345678902",
# 						"currency":"USD",
# 						"payment_method":"Visa 2345",
# 						"order_url":"http://petersapparel.parseapp.com/order?order_id=123456",
# 						"timestamp":"1428444852",
# 						"address":{
# 						  "street_1":"1 Hacker Way",
# 						  "street_2":"",
# 						  "city":"Menlo Park",
# 						  "postal_code":"94025",
# 						  "state":"CA",
# 						  "country":"US"
# 						},
# 						"summary":{
# 						  "subtotal":75.00,
# 						  "shipping_cost":4.95,
# 						  "total_tax":6.19,
# 						  "total_cost":56.14
# 						},
# 						"adjustments":[
# 						  {
# 							"name":"New Customer Discount",
# 							"amount":20
# 						  },
# 						  {
# 							"name":"$10 Off Coupon",
# 							"amount":10
# 						  }
# 						],
# 						"elements":[
# 						  {
# 							"title":"Classic White T-Shirt",
# 							"subtitle":"100% Soft and Luxurious Cotton",
# 							"quantity":2,
# 							"price":50,
# 							"currency":"USD",
# 							"image_url":"http://petersapparel.parseapp.com/img/whiteshirt.png"
# 						  },
# 						  {
# 							"title":"Classic Gray T-Shirt",
# 							"subtitle":"100% Soft and Luxurious Cotton",
# 							"quantity":1,
# 							"price":25,
# 							"currency":"USD",
# 							"image_url":"http://petersapparel.parseapp.com/img/grayshirt.png"
# 						  }
# 						]
# 					  }
# 					}
# 				}
#
# 		dispatcher.utter_custom_json(res)
# 		print(res)
# 		res1 = {
# 			"text": "Any more questions? ",
#
# 			   "quick_replies": [
# 			{
# 				"content_type": "text",
# 				"title": "Display Reviews",
# 				"payload": "Display Reviews"
# 			},
# 			{
# 				"content_type": "text",
# 				"title": "No, Thankyou",
# 				"payload": "No, Thankyou"
# 			}
#
# 		]
# 		}
# 		dispatcher.utter_custom_json(res1)