import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { UtilDialogData } from '../../interfaces/UtilDialogData';

@Component({
  selector: 'app-util-dialog',
  templateUrl: './util-dialog.component.html',
  styleUrls: ['./util-dialog.component.scss'],
})
export class UtilDialogComponent implements OnInit {
  // ダイアログ選択結果
  selectResult: boolean;
  constructor(
    public dialogRef: MatDialogRef<UtilDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: UtilDialogData
  ) {}

  ngOnInit(): void {
    this.selectResult = false;
  }

  onCancelClick(): void {
    this.selectResult = false;
    this.dialogRef.close();
  }
}
