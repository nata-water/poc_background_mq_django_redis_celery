import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UtilDialogComponent } from './util-dialog.component';

describe('UtilDialogComponent', () => {
  let component: UtilDialogComponent;
  let fixture: ComponentFixture<UtilDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UtilDialogComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UtilDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
