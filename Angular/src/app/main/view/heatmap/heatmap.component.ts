import { Component, OnInit, ViewChild } from '@angular/core';
import { NgxSpinnerService } from 'ngx-spinner';
import { DataService } from '../../data.service';
import { HeatmapInfoService } from '../../heatmap-info.service';
import { CanvasComponent } from './canvas/canvas.component';
import { PlotlyComponent } from './plotly/plotly.component';


@Component({
  selector: 'app-heatmap',
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.css']
})
export class HeatmapComponent implements OnInit {

  @ViewChild(CanvasComponent) canvas: CanvasComponent;
  @ViewChild(PlotlyComponent) plotly: PlotlyComponent;

  public formdata: Object;

  public src: string = "no_heatmap";
  public img: HTMLImageElement;
  public imgLoading: boolean = false;
  public plotlyBool: boolean = false;

  constructor(private dataService: DataService,
              private heatmapInfoService: HeatmapInfoService,
              private spinner: NgxSpinnerService,
            ) { }

  ngOnInit(): void {
    this.spinner.show();
    this.heatmapInfoService.plotlyBool.subscribe(bool => {this.plotlyBool = bool;});
    this.dataService.submittedData.subscribe(data => {
      this.formdata = data;
      if (this.plotlyBool) {
        this.plotly.getPlotly(this.formdata);
      } else {
        this.setImg();
      }
    });
  }

  setImg(): void{
    this.imgLoading = true;
    this.dataService.get_blob('heatmap', this.formdata).subscribe(img => {
      this.imgFromBlob(img);
    }, error => {
      this.imgLoading = false;
      this.heatmapInfoService.img_loaded(false);
      console.log(error);
    });
  }

  setSrc(src: string): void{
    this.src = src;
  }

  imgFromBlob(img: Blob) {
    console.log("Getting URL from Blob");
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.setSrc(reader.result as string);
      this.canvas.setImg(this.src);
      this.imgLoading = false;
      this.heatmapInfoService.img_loaded(true);
      console.log("Heatmap src changed to: ", this.src);
    }, false);

    if (img) {
      reader.readAsDataURL(img);
    }
  }


}
