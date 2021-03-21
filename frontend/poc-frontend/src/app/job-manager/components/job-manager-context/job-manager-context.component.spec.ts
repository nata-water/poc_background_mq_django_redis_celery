import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobManagerContextComponent } from './job-manager-context.component';

describe('JobManagerContextComponent', () => {
  let component: JobManagerContextComponent;
  let fixture: ComponentFixture<JobManagerContextComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ JobManagerContextComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(JobManagerContextComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
