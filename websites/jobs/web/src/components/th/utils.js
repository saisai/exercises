import { DataGrid } from '@mui/x-data-grid';


export function getUrl(params) {
    return (
        <a target='_blank'  rel="noreferrer"  href={params.row.link}>{params.row.title}</a>
    );    
  }

export const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'title', headerName: 'Title', width: 700,
        renderCell: getUrl,
    },
    { field: 'time', headerName: 'Time', width: 600 }
]

export const URL = "http://127.0.0.1:8888/";

export const footers = [
    {
      title: 'Company',
      description: ['Team', 'History', 'Contact us', 'Locations'],
    },
    {
      title: 'Features',
      description: [
        'Cool stuff',
        'Random feature',
        'Team feature',
        'Developer stuff',
        'Another one',
      ],
    },
    {
      title: 'Resources',
      description: ['Resource', 'Resource name', 'Another resource', 'Final resource'],
    },
    {
      title: 'Legal',
      description: ['Privacy policy', 'Terms of use'],
    },
  ];

export function ShowDataGrid({data, columns}) {
  return (
      <>
        <DataGrid
            rows={data}
            columns={columns}                
            initialState={{
            ...data.initialState,
            pagination: { paginationModel: { pageSize: 25 } },
            }}
            pageSizeOptions={[25, 50, 75, 100]}
            />     
      </>
  );
}
