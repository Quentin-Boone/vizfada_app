import { Component, Input, OnInit } from '@angular/core';
import { HLFilterComponent } from '../../../utils/hlfilter';
import { HeatmapInfoService } from '../../heatmap-info.service';



@Component({
  selector: 'app-highlight',
  templateUrl: './highlight.component.html',
  styleUrls: ['./highlight.component.css']
})
export class HighlightComponent extends HLFilterComponent implements OnInit {
  @Input() color: string;

  constructor(heatmapInfoService: HeatmapInfoService) {
    super(heatmapInfoService)
  }

  ngOnInit(): void {
    super.ngOnInit();
  }

  onChangeColor(e): void {
    this.color = e;
    this.formGroup.controls['color'].setValue(e.substr(1));
    console.log("Changing color to ", e);
  }
  
  /*
  getValues(e): void {
    let selected = e;
    console.log("Selected ", selected)
    this.formGroup.controls['field'].setValue(selected);
    this.dataService.get_fields(this.formGroup.value)
                    .subscribe(meta => {this.METADATA = meta});
    this.values = this.METADATA[selected]["values"]
  }

  addSelected(e): void {
    this.selectedValues.push(e);
  }

  removeSelected(e): void {
    let i=this.selectedValues.indexOf(e);
    console.log(e, " found at ", i, " in ", this.selectedValues)
    this.selectedValues.splice(i, 1);
    console.log(this.selectedValues)
  }

  onSelectValue(e): void {
    let selected = this.addSelected(e);
    console.log("Selected value ", e);
    this.formGroup.controls['values'].setValue(this.selectedValues);
    console.log("Currently selected ", this.formGroup.controls['values'])
  }
  */

}
