# #!/usr/bin/env python3
# from ebaysdk.trading import Connection
#
# if __name__ == '__main__':
#     api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
#     request = {
#         "Item": {
#             "Title": "Professional Mechanical Keyboard",
#             "Country": "US",
#             "Location": "JP",
#             "Site": "US",
#             "ConditionID": "1000",
#             "PaymentMethods": "PayPal",
#             "PayPalEmailAddress": "nobody@gmail.com",
#             "PrimaryCategory": {"CategoryID": "33963"},
#             "Description": "A really nice mechanical keyboard!",
#             "ListingDuration": "Days_10",
#             "StartPrice": "150",
#             "Currency": "USD",
#             "ReturnPolicy": {
#                 "ReturnsAcceptedOption": "ReturnsAccepted",
#                 "RefundOption": "MoneyBack",
#                 "ReturnsWithinOption": "Days_30",
#                 "Description": "If you are not satisfied, return the keyboard.",
#                 "ShippingCostPaidByOption": "Buyer"
#             },
#             "ShippingDetails": {
#                 "ShippingServiceOptions": {
#                     "FreeShipping": "True",
#                     "ShippingService": "USPSMedia"
#                 }
#             },
#             "DispatchTimeMax": "3"
#         }
#     }
#
# api.execute("AddItem", request)

#!/usr/bin/env python3
from ebaysdk.trading import Connection

if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        "Item": {
            # geography
            "Country": "JP",
            "Location": "Tokyo",
            "Site": "US",

            # payments
            "AutoPay": "True",
            "BestOfferDetails": {
                "BestOfferEnabled": "True",
            },
            # "CrossBorderTrade": "UK", # This costs $0.50: https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4364
            "Currency": "USD",
            "DispatchTimeMax": "1",
            "ListingDuration": "GTC",
            "ListingType": "FixedPriceItem",
            "PaymentMethods": "PayPal",
            # "PayPalEmailAddress": "eddzgfx+paypal@gmail.com",
            "PayPalEmailAddress": "sb-8faft943977@business.example.com",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsAccepted",
                "RefundOption": "MoneyBack",
                "ReturnsWithinOption": "Days_30",
                "ShippingCostPaidByOption": "Buyer"
            },

            # shipping
            "ShippingDetails": {
                "GlobalShipping": "True",
                "InternationalShippingServiceOption": [
                    {
                        "ShippingService": "StandardInternational", # https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCodeType.html
                        "ShippingServiceCost": "6.00",
                        "ShippingServicePriority": "1", # 1 is highest, 5 is lowest
                        "ShipToLocation": ["DE", "FR", "GB"],
                    },
                    {
                        "ShippingService": "EconomyShippingFromOutsideUS", # https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCodeType.html
                        "ShippingServiceCost": "2.50",
                        "ShippingServicePriority": "2", # 1 is highest, 5 is lowest
                        "ShipToLocation": ["DE", "FR", "GB"],
                    },
                    {
                        "ShippingService": "ExpeditedInternational", # https://developer.ebay.com/devzone/xml/docs/reference/ebay/types/ShippingServiceCodeType.html
                        "ShippingServiceCost": "20.00",
                        "ShippingServicePriority": "3", # 1 is highest, 5 is lowest
                        "ShipToLocation": ["DE", "FR", "GB"],
                    },
                ],
                "ShippingServiceOptions": [
                    {
                        "FreeShipping": "False",
                        "ShippingService": "StandardShippingFromOutsideUS",
                        "ShippingServiceCost": "6.00",
                        "ShippingServicePriority": "1", # 1 is highest, 5 is lowest
                    },
                    {
                        "FreeShipping": "False",
                        "ShippingService": "EconomyShippingFromOutsideUS",
                        "ShippingServiceCost": "2.50",
                        "ShippingServicePriority": "2", # 1 is highest, 5 is lowest
                    },
                    {
                        "FreeShipping": "False",
                        "ShippingService": "ExpeditedShippingFromOutsideUS",
                        "ShippingServiceCost": "20.00",
                        "ShippingServicePriority": "3", # 1 is highest, 5 is lowest
                    },
                ],
            },

            "PrimaryCategory": {
                # 2611 = Toys & Hobbies|Collectible Card Games|Pokemon Trading Card Game|Pokemon Individual Cards
                "CategoryID": "2611",
            },

            # item specifics
            "ConditionID": "3000", # https://developer.ebay.com/DevZone/guides/features-guide/default.html#development/Desc-ItemCondition.html\
            # Title structure:
            #     POKEMON NAME
            #     Rarity
            #     "Japanese"
            #     Set Name English
            #     #XXX (Pokemon number)
            #     " - Pokemon card"
            #     set append text e.g. " - no shadowless rarity" (base set)
            #     card append text e.g. " BANNED naked Kasumi" (Misty's tears)
            "Title": "CHARIZARD Holo Japanese 1st Base Set #006 - Pokemon Card No Shadowless Rarity",
            "Description": "replaceme",
            "ListingDetails": {
                "BestOfferAutoAcceptPrice": "9.00",
                "MinimumBestOfferPrice": "8.00",
            },
            "ItemSpecifics": {
                "NameValueList": [
                    {
                        "Name":  "Set",
                        "Value": "Gym Heroes",
                    },
                    {
                        "Name":  "Language",
                        "Value": "Japanese",
                    },
                    {
                        "Name":  "Card Type",
                        "Value": "Trainer|Pokemon|Energy|etc",
                    },
                    {
                        "Name":  "Country/Region of Manufacture",
                        "Value": "Japan",
                    },
                    {
                        "Name":  "Brand",
                        "Value": "Nintendo|Wizards of the Coast", # surprisingly no "Pokemon"
                    },
                    {
                        "Name":  "Energy Type",
                        "Value": "Grass|Fire|Dragon|Metal|etc",
                    },
                    {
                        # Altered Art|First Edition|Full Art|Holo|Miscut|Misprint|Oversized|Shadowless|etc
                        "Name":  "Features",
                        "Value": "First Edition",
                        "Value": "Holo",
                        "Value": "Shadowless",
                    },
                    # {
                    #     "Name":  "Modified Item",
                    #     "Value": "No|Yes",
                    # },
                    # # {
                    # #     # only if "Modified Item" is set to "Yes"
                    # #     "Name":  "Signed",
                    # #     "Value": "No|Yes",
                    # # },
                    {
                        "Name":  "Featured Cards",
                        "Value": "Ancient Mew|Charizard 4/102|Happy Birthday Pikachu|Legendary Pokemon|Venusaur|etc",
                    },
                    {
                        "Name":  "Grade",
                        "Value": "0.5|1|1.5|...|9.5|10|custom",
                    },
                    {
                        "Name":  "Professional Grader",
                        "Value": "PSA|BCCG|BGS|SGC|custom",
                    },
                    {
                        "Name":  "Rarity",
                        "Value": "Common|Uncommon|Ultra Rare|Secret Rare|Rare|Holofoil Rare|custom",
                    },
                    {
                        "Name":  "Language",
                        "Value": "Japanese",
                    },
                ]
            },
            "Quantity": "1", # if want to set to > 1, have a look at creating "variants" of this listing
            "StartPrice": "12.34", # the actual price
            "UUID": "12345678d0123aaa7890123a56789a12", # unique internal identifier (e.g. stock id)

            # # pictures
            # "PictureDetails": {
            #     "PictureSource": "Vendor", # means "self-hosted"
            #     # Must have at least one image
            #     # Must be https
            #     # w+h must be < 12,000px
            #     # < 12MB
            #     # JPG, BMP, GIF, TIF, or PNG
            #     # "Images cannot have seller-added text or seller-added artwork" apparently
            #     "PictureURL": "https://mypicserver.com/myphoto1.jpg",
            #     "PictureURL": "https://mypicserver.com/myphoto2.jpg",
            # },

            # "ScheduleTime": "2004-08-04T19:09:02.768Z", # UTC
        }
    }

    api.execute("AddFixedPriceItem", request)
