import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Unstable_Grid2';



import Checkboxes from '../checkbox/Checkboxes'
import ControlledCheckbox from '../checkbox/ControlledCheckbox'
import FloatingActionButtons from '../floating-action-button/FloatingActionButtons'
import Asynchronous from './Autocomplete/Asynchronous'
import ComboBox from './Autocomplete/autocomplete'
import Playground from './Autocomplete/AutoCompleteplayground'
import BasicButtonGroup from './button-group/BasicButtonGroup'
import SplitButton from './button-group/SplitButton'
import BasicButtons from './Button/BasicButtons'
import UploadButtons from './Button/UploadButtons'
import BasicSelect from '../select/BasicSelect';
import ControlledSwitches from '../switch/ControlledSwitches';
import SimpleBadge from '../badge/SimpleBadge';
import BasicTable from '../table/BasicTable';
import DataTable from '../table/DataTable';
import EnhancedTable from '../table/EnhancedTable';
import BasicAlerts from '../alert/BasicAlerts';
import AlertDialog from '../dialog/AlertDialog';
import Variants from '../skeleton/Variants';
import SimpleSnackbar from '../snackbar/SimpleSnackbar';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

  export default function Main() {
    return (
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={2}>
          <Grid xs={4}>
            <Item>xs=8</Item>
            <ComboBox />
            <ComboBox />
            <Asynchronous />
            <BasicButtons />
            <UploadButtons />

            <BasicButtonGroup />
            <SplitButton />

            <Checkboxes />
            <ControlledCheckbox />

            <FloatingActionButtons />
          </Grid>
          <Grid xs={4}>
            <BasicSelect />
            <ControlledSwitches />
            <SimpleBadge />
            <BasicAlerts />
            <AlertDialog />
            <Variants />
            <SimpleSnackbar />
          </Grid>
          <Grid xs={4}>
            <Item>xs=4</Item>
            <BasicTable />
            <DataTable />
            <EnhancedTable />
          </Grid>         
        </Grid>
      </Box>
    );
  }

{/* <Playground /> */}
/*
export default function Main () {
    return (
            <>
            <ComboBox />
            <ComboBox />
            <Asynchronous />

            <BasicButtons />
            <UploadButtons />

            <BasicButtonGroup />
            <SplitButton />

            <Checkboxes />
            <ControlledCheckbox />

            <FloatingActionButtons />
            
            </>

    )
}

*/