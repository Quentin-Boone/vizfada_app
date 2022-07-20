import { Component, OnInit } from '@angular/core';
import { DataService } from '../../../data.service';
import { HeatmapInfoService } from '../../../heatmap-info.service';


@Component({
  selector: 'app-legend',
  templateUrl: './legend.component.html',
  styleUrls: ['./legend.component.css']
})
export class LegendComponent implements OnInit {

  public data: Object;
  public legend: Object;
  public selectedColor: string;

  constructor(private dataService: DataService,
              private heatmapInfoService: HeatmapInfoService,) { }

  ngOnInit(): void {
    this.heatmapInfoService.pxcolor.subscribe(color => {
      this.selectedColor = color as string;
    })
    this.heatmapInfoService.imgLoaded.subscribe(value => {
      if (value === true) {
        this.get_legend();
      }
    })
    /*
    this.dataService.submittedData.subscribe(data => {
      this.data = data;
      this.get_legend(this.data)
    });
    */
  }

  get_legend(): void {
    this.dataService.get_json('legend').subscribe(legend => {
      console.log(legend);
      this.legend = legend;
      for (let leg in legend) {
        this.legend[leg] = this.rgb_conversion(legend[leg]);
      }
      console.log(this.legend);
    })
  }

  rgb_conversion(rgb: Array<number>): string {
    const r=(rgb[0] * 255).toFixed();
    const g=(rgb[1] * 255).toFixed();
    const b=(rgb[2] * 255).toFixed();
    return(`rgb(${r}, ${g}, ${b})`);
  }

}
