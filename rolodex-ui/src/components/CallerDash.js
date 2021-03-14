import React, {useState, useEffect} from "react"
import Score from './Score'
import CustomizedTables from './CustomizedTables'
import s from '../styles/callerdash.module.css';



import axios from 'axios';


const CallerDash = () => {
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
        <div className={s.container}>
           <h3 className={s.titleBar}>Call Center - Recent Calls Dashboard</h3>
           <div className={s.dashWidgets}>
              <div className={s.callTbl}>
                 <CustomizedTables callData={data}/>
              </div>
              <div className={s.scoreWidg}>
                 <Score callData={data.data}/>
              </div>
           </div>
        </div>
    )
}

export default CallerDash;