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
        return buttons
    def populate_all(self):
        self.populate_school_subscriptions()

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

        # 6
        db.school_subscriptions.insert(
            Archived=False,
            MembershipRequired=False,
            Name='Unit not defined',
            Classes=1,
            CreditValidity=28,  # 4 weeks
            SubscriptionUnit=None,
            SortOrder=0,
            QuickStatsAmount=12.5
        )

        # 7
        db.school_subscriptions.insert(
            Archived=False,
            MembershipRequired=False,
            Name='Classes not defined',
            Classes=None,
            CreditValidity=28,  # 4 weeks
            SubscriptionUnit='month',
            SortOrder=0,
            QuickStatsAmount=5
        )

        ss_one_price = 40
        db.school_subscriptions_price.insert(
            school_subscriptions_id=1,
            Startdate='1900-01-01',
            Price=ss_one_price)

        db.school_subscriptions_price.insert(
            school_subscriptions_id=2,
            Startdate='1900-01-01',
            Price=0)

        db.commit()

