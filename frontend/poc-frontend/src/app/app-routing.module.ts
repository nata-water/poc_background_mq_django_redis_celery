import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { JobProcessComponent } from './job-manager/components/job-process/job-process.component';
import { JobResultComponent } from './job-manager/components/job-result/job-result.component';

const routes: Routes = [
  { path: '', component: JobProcessComponent },
  { path: 'result', component: JobResultComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
