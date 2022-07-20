import { TestBed } from '@angular/core/testing';

import { HeatmapInfoService } from './heatmap-info.service';

describe('HeatmapInfoService', () => {
  let service: HeatmapInfoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HeatmapInfoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
