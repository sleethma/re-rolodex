import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

function createData(uuid, ani, vanityNum, score, timestamp) {
  return { uuid, ani, vanityNum, score, timestamp};
}


const useStyles = makeStyles({
  table: {
    align: "center",
    minWidth: 700,
  },
});

let rows = [];

const genRows = (callData) =>{
  console.log("callData print ", callData);
  
  callData.data.map(item =>(
    console.log('id: ', item.uuid)
    ))

  callData.data.map(item =>(
    rows.push(createData(item.uuid, item.callers_num,  item.vanity_number, item.score,item.timestamp))
    ))
};


export default function CustomizedTables({callData}) {
  const classes = useStyles();

  if(callData['data'].length !== 0){
    console.log('Call data not 0', callData)
    genRows(callData);
  }

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell>Callers Ani</StyledTableCell>
            <StyledTableCell align="right">Vanity Number</StyledTableCell>
            <StyledTableCell align="right">Score</StyledTableCell>
            <StyledTableCell align="right">Inbound Call DateTime</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <StyledTableRow key={row.uuid}>
              <StyledTableCell align="left">{row.ani}</StyledTableCell>
              <StyledTableCell align="right">{row.vanityNum}</StyledTableCell>
              <StyledTableCell align="right">{row.score}</StyledTableCell>
              <StyledTableCell align="right">{row.timestamp}</StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
