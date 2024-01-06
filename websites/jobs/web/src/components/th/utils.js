
export function getUrl(params) {

    console.log(params.row.title);
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
