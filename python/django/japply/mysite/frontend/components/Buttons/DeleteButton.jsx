import React, { memo } from "react";
import { Button } from "@material-ui/core";
import { EditOutlined as EditIcon } from "@material-ui/icons";
import useStyles from "./styles";
import { ToolbarButtonProps } from "../Types";

export const EditButton = memo(({ rows = [] }: ToolbarButtonProps) => {
  const classes = useStyles();

  const isDisable = !(rows.length === 1);

  const handleClick = () => {
    console.log("Editar", rows);
  };

  return (
    <Button
      startIcon={<EditIcon />}
      className={classes.button}
      onClick={handleClick}
      disabled={isDisable}
    >
      Editar
    </Button>
  );
});