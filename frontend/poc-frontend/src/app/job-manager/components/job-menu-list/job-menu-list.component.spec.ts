import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobMenuListComponent } from './job-menu-list.component';

describe('JobMenuListComponent', () => {
  let component: JobMenuListComponent;
  let fixture: ComponentFixture<JobMenuListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ JobMenuListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(JobMenuListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
