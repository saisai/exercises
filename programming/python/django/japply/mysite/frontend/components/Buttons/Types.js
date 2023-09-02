import { GridRowData } from "@material-ui/data-grid";

export type ToolbarButtonProps = {
  name: string;
  rows?: GridRowData[];
  totalRows?: number;
}