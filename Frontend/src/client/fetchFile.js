/* 
    JavaScript REST Query client which communicates with the Django backend.
    Proudly making use of the axios library.
*/

import axios from "axios";

export const GetUsers = (id=null) => {
    /* Function to fetch user data from the Django backend */
    if(id === null) { 
        axios.get('/api/users/').then(response => {
            return response;
        }).catch(err => {
            return err;
        })
    }
    
    axios.get(`/api/users/${id}`).then(response => {
        return response.data;
    }).catch(err => {
        return err;
    })
}

export const GetIdeas = (id=null) => {
    /* Function to fetch ideas from the Django backend */
    if(id === null) { 
        axios.get('/api/ideas/').then(response => {
            return response.data;
        }).catch(err => {
            return err;
        })
    }
    axios.get(`/api/ideas/${id}`).then(response => {
        return response.data;
    }).catch(err => {
        return err;
    })
}


