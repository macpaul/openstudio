import React, { Component } from "react"
import { intlShape } from "react-intl"
import PropTypes from "prop-types"

import PageTemplate from "../../../components/PageTemplate"
import BookOptionsList from "./BookOptionsList"


class Book extends Component {
    constructor(props) {
        super(props)
        console.log(props)
    }

    PropTypes = {
        intl: intlShape.isRequired,
        fetchBookingOptions: PropTypes.function,
        setPageTitle: PropTypes.function,
        app: PropTypes.object,
        options: PropTypes.object,
    }

    componentWillMount() {
        this.props.setPageTitle(
            this.props.intl.formatMessage({ id: 'app.pos.checkin.page_title' })
        )

        console.log(this.props.match.params.clsID)
        console.log(this.props.match.params.cuID)
        this.props.fetchBookingOptions(this.props.match.params.clsID, this.props.match.params.cuID )
    }

    render() {
        const booking_options = this.props.options.data
        

        return (
            <PageTemplate app_state={this.props.app}>
                { 
                    (!this.props.options.loaded) ? 
                        <div>Loading booking options, please wait...</div> :
                        <section className="checkin_attendance">
                            <BookOptionsList booking_options={booking_options} />
                            {/* <AttendanceList attendance_items={this.props.attendance.data} /> */}
                        </section>
                }
            </PageTemplate>
        )
    }
}

export default Book
