# -*- coding: utf-8 -*-

# from populate_os_tables import  *
from gluon import *
from os_gui import *

class PopulateDemoData:
    """
    This class populates the db database with test data for the test server
    """
    def get_buttons(self):
        os_gui = OsGui()
        buttons = os_gui.get_button('add',
                                       URL(self.populate_all()),
                                       title='Populate All')

        buttons += os_gui.get_button('add',
                                       URL(self.populate_tax_rates()),
                                       title='Populate Tax Rates')

        buttons += os_gui.get_button('add',
                                       URL(self.populate_school_subscriptions()),
                                       title='Populate School Subscriptions')

        buttons += os_gui.get_button('add',
                                       URL(self.populate_school_classcards()),
                                       title='Populate School Classcards')

        buttons += os_gui.get_button('add',
                                       URL(self.populate_school_memberships()),
                                       title='Populate School Memberships')

        buttons += os_gui.get_button('add',
                                       URL(self.populate_auth_user_teachers()),
                                       title='Populate Teachers')
        return buttons
    def populate_all(self):
        self.populate_tax_rates()
        self.populate_school_subscriptions()
        self.populate_auth_user_teachers()
        self.populate_school_classcards()
        self.populate_school_memberships()


    def populate_tax_rates(self):
       db = current.db

       db.tax_rates.insert(
            Name='BTW 21%',
            Percentage=21
            )

       db.tax_rates.insert(
            Name='BTW 6%',
            Percentage=6
        )


    def populate_school_subscriptions(self):
        db = current.db

        # 1
        db.school_subscriptions.insert(
            Archived=False,
            PublicSubscription=True,
            MembershipRequired=False,
            Name='one class a week',
            Classes=1,
            SubscriptionUnit='week',
            CreditValidity=28,  # 4 weeks
            Terms='Subscription terms go here and I want to eat a watermelon',
            SortOrder=0,
            QuickStatsAmount=10
        )

        # 2
        db.school_subscriptions.insert(
            Archived=False,
            MembershipRequired=False,
            Name='Unlimited for free',
            Classes=0,
            CreditValidity=28,  # 4 weeks
            Unlimited=True,
            SortOrder=0,
            QuickStatsAmount=15
        )


        # 3
        db.school_subscriptions.insert(
            Archived=False,
            PublicSubscription=True,
            MembershipRequired=True,
            Name='Membership one class a week',
            Classes=1,
            SubscriptionUnit='week',
            CreditValidity=28,  # 4 weeks
            Terms='Subscription terms go here and I want to eat a watermelon',
            SortOrder=0,
            QuickStatsAmount=10
        )

        # 4
        db.school_subscriptions.insert(
            Archived=False,
            MembershipRequired=True,
            Name='Membership Unlimited for free',
            Classes=0,
            CreditValidity=28,  # 4 weeks
            Unlimited=True,
            SortOrder=0,
            QuickStatsAmount=15
        )

        # 5
        db.school_subscriptions.insert(
            Archived=False,
            MembershipRequired=False,
            Name='one class a month',
            Classes=1,
            CreditValidity=28,  # 4 weeks
            SubscriptionUnit='month',
            SortOrder=0,
            QuickStatsAmount=17.5
        )


        # ss_one_price = 40
        # db.school_subscriptions_price.insert(
        #     school_subscriptions_id=1,
        #     Startdate='1900-01-01',
        #     Price=ss_one_price)
        #
        # db.school_subscriptions_price.insert(
        #     school_subscriptions_id=2,
        #     Startdate='1900-01-01',
        #     Price=0)

    def populate_auth_user_teachers(self,
                                    teaches_classes=True,
                                    teaches_workshops=True):
        """
            Adds 2 teachers to db.
            auth.user.ids 2 and 3
        """
        db = current.db

        # try:
        #     populate_tax_rates(web2py)
        # except:
        #     print T('Tried to insert tax rates, but one or more already exists in db.tax_rates')
        #
        try:
            db.auth_user.insert(
                first_name = 'first',
                last_name  = 'teacher',
                email      = 'teacher@openstudioproject.com',
                teacher    = True,
                teaches_classes = teaches_classes,
                teaches_workshops = teaches_workshops
            )

            db.auth_user.insert(
                first_name = 'second',
                last_name  = 'teacher',
                email      = 'teacher2@openstudioproject.com',
                teacher    = True,
                teaches_classes = teaches_classes,
                teaches_workshops = teaches_workshops
            )




        except:
            print "Tried inserting teachers, but id 2 or 3 already exists in auth_user"


    # def populate_customers(self,
    #                        nr_of_customers=10,
    #                        tax_rates=True,
    #                        employee=False,
    #                        teacher=False,
    #                        created_on=datetime.datetime.now()):
    #     if tax_rates:
    #         populate_tax_rates(web2py)
    #
    #     populate(web2py.db.school_discovery, 3)
    #     populate_school_locations(web2py, 2)
    #     populate(web2py.db.school_levels, 3)
    #     populate(web2py.db.school_languages, 2)
    #
    #     for i in range(1, nr_of_customers+1):
    #         if i < 6:
    #             school_locations_id = 1
    #         else:
    #             school_locations_id = 2
    #
    #         cuID = i + 1000 # avoid conflict with teachers when populating
    #
    #         db.auth_user.insert(
    #             id                  = cuID,
    #             archived            = False,
    #             first_name          = 'customer_' + unicode(i),
    #             last_name           =  unicode(i),
    #             email               = 'customer' + unicode(i) + '@email.nl',
    #             customer            = True,
    #             city                = 'city_' + unicode(i),
    #             postcode            = '190-' + unicode(cuID) + 'A',
    #             school_locations_id = school_locations_id,
    #             employee=employee,
    #             teacher=teacher,
    #             created_on=created_on)
    #
    #     web2py.db.commit()
    #

    def populate_school_classcards(self,
            nr=1,
            trialcard=True,
            membership_required=False):
        """
            Add 'nr' of cards to school_classcards
        """
        db = current.db

        i = 0
        for i in range(i, nr):
            db.school_classcards.insert(
                PublicCard = True,
                MembershipRequired = membership_required,
                Name = 'Classcard_' + unicode(i),
                Description = 'General card ' + unicode(i),
                Price = 125,
                Validity = 3,
                ValidityUnit = 'months',
                Classes = 10,
                Trialcard = False)

        db.school_classcards.insert(
                    PublicCard = True,
                    MembershipRequired = True,
                    Name = 'Membership Classcard_' + unicode(i),
                    Description = 'General card ' + unicode(i),
                    Price = 125,
                    Validity = 3,
                    ValidityUnit = 'months',
                    Classes = 10,
                    Trialcard = False)

        if trialcard:
            db.school_classcards.insert(
                PublicCard = True,
                MembershipRequired = membership_required,
                Name = 'Proefweek',
                Description = 'General trialcard',
                Price = 15,
                Validity = 7,
                ValidityUnit = 'days',
                Trialcard = True)




    def populate_school_memberships(self, price=True):
       """
            Add a membership with a price
        """
       db = current.db


       db.school_memberships.insert(
            Archived = False,
            Name = 'Premium membership',
            Description = 'premium membership',
            Terms = "Mango season",
            Validity = 1,
            ValidityUnit = 'months'
           )

       if price:
           db.school_memberships_price.insert(
               school_memberships_id = 1,
               Startdate = '1900-01-01',
               Price = 40,
               tax_rates_id=1)


