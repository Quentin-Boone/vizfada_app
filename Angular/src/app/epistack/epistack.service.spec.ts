import { TestBed } from '@angular/core/testing';

import { EpistackService } from './epistack.service';

describe('EpistackService', () => {
  let service: EpistackService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EpistackService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
