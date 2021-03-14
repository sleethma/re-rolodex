import React from "react"
import s from '../styles/score.module.css';

const getAvgScore = (callData) => {
    let initialValue = 0
    let sum = callData.reduce(
    (accumulator, currentValue) => accumulator + parseInt(currentValue.score)
    , initialValue
)
    return sum/callData.length
}

const Caller = (props) => {
    let avgScore = 0;
    
    // TODO: below check b/c re-rendered by strict mode? Not issue in prod build.
    if(props.callData.length !== 0){
        avgScore = getAvgScore(props.callData)
      }

    return(
        <div className={s.container}>
           {avgScore > 0 &&
           <div className={s.scoreCont}>
              <div className={s.avgScoreTitle}> AVG SCORE </div>
              <div className={s.score}>
                 {avgScore}
              </div>
           </div>
           }
        </div>
    )
}

export default Caller;