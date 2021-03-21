import { Component, OnInit } from '@angular/core';
import { ProcessResourceService } from '../../services/process-resource.service';
import { BinaryResource } from '../../interfaces/BinaryResource';
import { Observable } from 'rxjs';
import { MatDialog } from '@angular/material/dialog';
import { UtilDialogComponent } from '../util-dialog/util-dialog.component';
import { UtilDialogData } from '../../interfaces/UtilDialogData';

@Component({
  selector: 'app-job-process',
  templateUrl: './job-process.component.html',
  styleUrls: ['./job-process.component.scss'],
})
export class JobProcessComponent implements OnInit {
  // 選択した処理対象ファイル情報
  processTargetResource: BinaryResource;

  // 対象ファイル一覧状態管理
  binaryResources: Observable<BinaryResource[]> = this.processResourceService
    .binaryResources$;

  constructor(
    private processResourceService: ProcessResourceService,
    public dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this.processResourceService.fetchBinaryResources();
  }

  // 処理実行ボタンクリック
  doProcessClick(): void {
    if (!this.processTargetResource) {
      return;
    }
    console.log(this.processTargetResource);

    // ダイアログ用データ
    const dialogData: UtilDialogData = {
      title: '実行確認',
      message: '実行してもよろしいですか？',
      cancelButtonText: 'キャンセル',
      okButtonText: 'OK',
    };

    const dialogRef = this.dialog.open(UtilDialogComponent, {
      width: '400px',
      data: dialogData,
    });

    // OKを選択:trueの場合に処理を実行する
    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.processResourceService
          .doParseResource(this.processTargetResource.id)
          .subscribe((_) => {
            // 実行後ダイアログ
            const dialogResultData: UtilDialogData = {
              title: '実行完了',
              message: '処理を実行しました。',
              okButtonText: 'OK',
            };
            const dialogResultRef = this.dialog.open(UtilDialogComponent, {
              width: '400px',
              data: dialogResultData,
            });
          });
      }
    });
  }
}
