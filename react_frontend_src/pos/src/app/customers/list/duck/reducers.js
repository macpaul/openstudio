import T from './types'


function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}


export const listReducer = (state = {}, action={ type: null }) => {
    switch (action.type) {
        case T.REQUEST_CUSTOMERS:
            return {
                ...state,
                loading: true,
                loaded: false,
                loading: action.loading,
            }
        case T.RECEIVE_CUSTOMERS:
            return {
                ...state,
                loading: false,
                loaded: true,
                data: action.data
            }
        case T.SET_CREATE_CUSTOMER_STATUS:
            return {
                ...state,
                create_customer: action.status
            }
        case T.SET_UPDATE_CUSTOMER_STATUS:
            return {
                ...state,
                update_customer: action.status
            }
        case T.REQUEST_CREATE_CUSTOMER:
            return {
                ...state,
                creating_customer: true,
                create_customer_temp_data: action.data
            }

        case T.RECEIVE_CREATE_CUSTOMER:           
            return {
                ...state,
                creating_customer: false,
                 data: {
                     ...state.data,
                     [action.data.result.id]: state.create_customer_temp_data
                },
                create_customer_error_data: action.data.result.errors
                
            }
        case T.REQUEST_UPDATE_CUSTOMER:
            return {
                ...state,
                updating_customer: true,
                update_customer_temp_data: action.data
            }
        case T.RECEIVE_UPDATE_CUSTOMER:
            if (!(isEmpty(action.data.result.errors))) {
                return {
                    ...state,
                    updating_customer: false,
                    update_customer_error_data: action.data.result.errors
                }
            } else {
                return {
                    ...state,
                    updating_customer: false,
                    data: {
                        ...state.data,
                        [action.data.id] : {
                            ...state.data[action.data.id],
                            ...state.update_customer_temp_data
                        }
                    },
                    update_customer_error_data: action.data.result.errors
                }
            }
        case T.REQUEST_SAVE_CAMERA_APP_SNAP:
            return {
                ...state,
                camera_app_snap_saving: true,
                camera_app_snap_saving: false
            }
        case T.RECEIVE_SAVE_CAMERA_APP_SNAP:
            console.log(action.data)
            if (action.data.status == 'fail') {
                console.log('failed')
                return {
                    ...state,
                    camera_app_snap_saving: false,
                    camera_app_snap_saving: true
                }
            } else {
                console.log('success')
                console.log(action.data.data.id)
                return {
                    ...state,
                    data: {
                        ...state.data,
                        [action.data.data.id] : {
                            ...state.data[action.data.data.id],
                            thumbsmall: action.data.data.thumbsmall,
                            thumblarge: action.data.data.thumblarge,
                        }
                    },
                    camera_app_snap: null,
                    camera_app_snap_saving: false,
                    camera_app_snap_saving: true
                }
            }
        case T.CLEAR_DISPLAY_CUSTOMER_ID:
            return {
                ...state,
                displayID: null,
            }
        case T.SET_DISPLAY_CUSTOMER_ID:
            return {
                ...state,
                displayID: action.id,
            }
        case T.CLEAR_SEARCH_TIMEOUT:
            return {
                ...state,
                searchTimeout: clearTimeout(state.searchTimeout), 
            }
        case T.SET_SEARCH_TIMEOUT:
            return {
                ...state,
                searchTimeout: action.timeout,
            }
        case T.CLEAR_SEARCH_CUSTOMER_ID:
            return {
                ...state,
                searchID: null,
            }
        case T.SET_SEARCH_CUSTOMER_ID:
            return {
                ...state,
                searchID: action.id,
            }
        case T.CLEAR_SEARCH_VALUE:
            return {
                ...state,
                search_value: "",
            }
        case T.SET_SEARCH_VALUE:
            return {
                ...state,
                search_value: action.value.toLowerCase(),
            }
        case T.CLEAR_SELECTED_CUSTOMER_ID:
            return {
                ...state,
                selectedID: null,
            }
        case T.SET_SELECTED_CUSTOMER_ID:
            return {
                ...state,
                selectedID: action.id,
            }
        case T.CLEAR_REDIRECT_NEXT_COMPONENT:
            return {
                ...state,
                redirect_next_component: null,
            }
        case T.SET_REDIRECT_NEXT_COMPONENT:
            return {
                ...state,
                redirect_next_component: action.component,
            }
        case T.SET_CAMERA_APP_SNAP:
            return {
                ...state,
                camera_app_snap: action.data
            }
        case T.CLEAR_CAMERA_APP_SNAP:
            return {
                ...state,
                camera_app_snap: null
            }
        default:
            return {
                ...state
            }
    }
}


