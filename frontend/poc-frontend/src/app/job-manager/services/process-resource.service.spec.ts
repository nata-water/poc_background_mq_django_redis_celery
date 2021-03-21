import { TestBed } from '@angular/core/testing';

import { ProcessResourceService } from './process-resource.service';

describe('ProcessResourceService', () => {
  let service: ProcessResourceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProcessResourceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
