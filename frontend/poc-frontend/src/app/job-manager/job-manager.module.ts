import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { JobManagerContextComponent } from './components/job-manager-context/job-manager-context.component';
import { JobMenuListComponent } from './components/job-menu-list/job-menu-list.component';
import { JobControlComponent } from './components/job-control/job-control.component';
import { JobProcessComponent } from './components/job-process/job-process.component';
import { JobResultComponent } from './components/job-result/job-result.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { RouterModule } from '@angular/router';
import { MatSelectModule } from '@angular/material/select';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { UtilDialogComponent } from './components/util-dialog/util-dialog.component';

@NgModule({
  declarations: [
    JobManagerContextComponent,
    JobMenuListComponent,
    JobControlComponent,
    JobProcessComponent,
    JobResultComponent,
    UtilDialogComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    HttpClientModule,
    // @angular/Materialモジュール
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule,
    MatSelectModule,
    MatButtonModule,
    MatDialogModule,
  ],
  exports: [
    JobManagerContextComponent,
    JobMenuListComponent,
    JobControlComponent,
    JobProcessComponent,
    JobResultComponent,
  ],
})
export class JobManagerModule {}
