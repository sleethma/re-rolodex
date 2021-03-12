// import React, {useState} from "react"
import React, {useState, useEffect} from "react"

import axios from 'axios';


const Caller = () => {
    const [data, setData] = useState({data: []});

    useEffect(() =>{
        const fetchData = async () => {
        const apiURL = 'https://6ndggcns55.execute-api.us-east-1.amazonaws.com/dev/rolodexServer'
        const response = await axios.get(apiURL);
        setData(response.data);
        };   
        fetchData();}    
        ,[]);

    return(
        <div>
        <h3>Call Center Stats</h3>
        <ul>{data.data.map(item =>(
            <li key={item.callers_num}> {item.vanity_number}</li>))}
        </ul>
        {/* <ul> {calls.data.map((call) => <li>{call.callers_num}</li>)}</ul> */}
        </div>
    )
}

export default Caller;