import { Component, OnInit } from '@angular/core';
import { DataService } from '../../../data.service';
import { HeatmapInfoService } from '../../../heatmap-info.service';


@Component({
  selector: 'app-plotly',
  templateUrl: './plotly.component.html',
  styleUrls: ['./plotly.component.css']
})
export class PlotlyComponent implements OnInit {
  public allData: any[];
  public layout: Object;
  public config: Object;
  public formdata: Object;
  
  constructor(private dataService: DataService,
              private heatmapInfoService: HeatmapInfoService ) { };
  
  ngOnInit(): void {
    this.allData = [];
    this.config = {};
    this.layout = {};
  };
  
  getPlotly(formdata: Object): void {
    this.allData=[];
    this.config = {responsive: true };
    console.log("Annotated heatmap?");
    console.log(formdata["annotated"]);
    console.log(formdata["annotated"] != "");
    this.dataService.get_json('plotly', formdata).subscribe(data => {
      console.log("Annotated plotly");
      console.log(data);
      if (data[0] === "") {
        this.allData.push(data[1]);
        this.layout = { title: "Heatmap", autosize: true};
      } else {
        this.allData.push(data[0]);
        this.allData.push(data[1]);
        console.log("Plotly data");
        console.log(this.allData);
        this.layout = {
                        title: "Heatmap", autosize: true,
                        grid: {rows:1,
                               columns:2,
                               subplots:[["xy", "x2y"]]},
                        xaxis: {domain: [0.0, 0.05]},
                        xaxis2: {domain: [0.1, 1]},
                        hoverlabel: {align: 'center'}
                      }
        this.heatmapInfoService.img_loaded(true);
      }
    });
  };
  
  changeData(data: Object): void {
    this.allData.push(data);
  };
  
  getLegend(): void {
    this.heatmapInfoService.img_loaded(true);
  };

};
