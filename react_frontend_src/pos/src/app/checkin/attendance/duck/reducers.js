import T from './types'

export const checkinAttendanceReducer = (state = {}, action={ type: null }) => {
    switch (action.type) {
        case T.CHECKIN_SET_CLASS_ATTENDANCE_LOADING:
            return {
                loading: action.loading,
                ...state
            }
        case T.CHECKIN_REQUEST_CLASS_ATTENDANCE:
            return {
                loading: true,
                loaded: false,
                data: {}
            }
        case T.CHECKIN_RECEIVE_CLASS_ATTENDANCE:
            return {
                loading: false,
                loaded: true,
                data: action.data.attendance,
            }
        case T.CHECKIN_SET_CLASS_ATTENDANCE_SEARCH_CUSTOMER_ID:
            return {
                search_customer_id: action.search_customer_id,
                ...state,
            }
        default:
            return {
                ...state
            }
    }
}
