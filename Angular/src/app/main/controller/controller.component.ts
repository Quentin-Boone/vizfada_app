import { Component, OnInit, ViewChild } from '@angular/core';
import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Fields } from '../../utils/metadata';
import { DataService } from '../data.service';
import { HeatmapInfoService } from '../heatmap-info.service';
import { LegendComponent } from '../view/heatmap/legend/legend.component';
import { Files } from 'ng-bootstrap-icons/icons';

@Component({
  selector: 'app-controller',
  templateUrl: './controller.component.html',
  styleUrls: ['./controller.component.css']
})
export class ControllerComponent implements OnInit {

  @ViewChild(LegendComponent) legend: LegendComponent;

  public FIELDS: Fields;
  public SPECIES: string[] = [];
  public EXPERIMENTS: string[] = [];
  public testFields: Fields;

  public fields: string[];
  public plotlyChecked: boolean = false;
  public speciesIsSet: boolean = false;
  public experimentIsSet: boolean = false;

  public formGroup: FormGroup;
  
  objectKeys = Object.keys;

  constructor(private builder: FormBuilder,
              private dataService: DataService,
              private heatmapInfoService: HeatmapInfoService,) { }

  ngOnInit(): void {
    let newForm = this.builder.group({
      species: ["", [Validators.required]],
      experiment: ["", [Validators.required]],
      filters: this.builder.array([]),
      highlights: this.builder.array([]),
      annotated: "",
      options: this.builder.group({}),
      file: ""
    });
    console.log(newForm);
    this.formGroup = newForm;
    this.dataService.get_list('species').subscribe(species => {this.SPECIES = species});
    this.heatmapInfoService.fields.subscribe(fields => {this.testFields = fields})

  }

  addFilter():void {
    this.getMetadata();
    console.log("Adding filter")
    const arrayControl = <FormArray>this.formGroup.controls['filters'];
    let newGroup = this.builder.group({
      field: ['', [Validators.required]],
      values: [[], [Validators.required]]
    });
    arrayControl.push(newGroup);
  }

  addHighlight(): void {
    console.log("Adding highlight")
    const arrayControl = <FormArray>this.formGroup.controls['highlights'];
    let newGroup = this.builder.group({
      field: ['', [Validators.required]],
      values: [[], [Validators.required]],
      color: ["0082ff", [Validators.required]]
    });
    arrayControl.push(newGroup);
    this.getMetadata()
  }

  getMetadata(): void {
    console.log(this.formGroup.value);
    //this.dataService.get_meta('fields', this.formGroup.value)
    //                .subscribe(meta => {this.FIELDS = meta; console.log(meta)});
    this.heatmapInfoService.update_formGroup(this.formGroup.value)
  }
  
  
  //getSize(): bool {}

  get formFilters() {return <FormArray>this.formGroup.get('filters')}

  get formHighlights() {return <FormArray>this.formGroup.get('highlights')}

  delFromArray(name: string, index: number): void {
    console.log("Removing filter")
    const arrayControl = <FormArray>this.formGroup.controls[name];
    arrayControl.removeAt(index);
    this.getMetadata()
  }

  changeExperiment(e) {
    console.log("Changing experiment")
    this.formGroup.controls['experiment'].setValue(e.target.value);
    if (e.target.value != "") {
      this.getMetadata();
      this.experimentIsSet = true;
    } else {
      this.experimentIsSet = false;
    }
    console.log("Experiment is set: ", this.experimentIsSet)
  }

  changeSpecies(e) {
    console.log("Changing species")
    this.formGroup.controls['species'].setValue(e.target.value);
    if (e.target.value != "") {
      this.dataService.get_list('experiments', this.formGroup.controls['species'].value).subscribe(experiment => {this.EXPERIMENTS=experiment.filter( str => !str.includes('.'))});
      this.speciesIsSet = true;
    } else {
      this.speciesIsSet = false;
    }
    console.log("Species is set: ", this.speciesIsSet)
  }

  changeSize(e) {
    console.log("Changing size")
    const s = e.target.value;
    let optionsControl = <FormGroup>this.formGroup.controls['options'];
    try {
      optionsControl.controls['figsize'].setValue(`(${s}, ${s})`);
    } catch (error) {
      optionsControl.addControl('figsize', new FormControl(`(${s}, ${s})`));
    }
    this.formGroup.controls['options'] = optionsControl;
  }

  changeAnnotation(e) {
    console.log("Changing annotated field to: ", e.target.value);
    this.formGroup.controls['annotated'].setValue(e.target.value);
  }
  

  changePlotlyBool(e) {
    console.log("Changing plotly bool:");
    console.log(e.target.checked);
    this.heatmapInfoService.set_plotlyBool(e.target.checked);
    this.plotlyChecked = e.target.checked;
  }

  fileChanged(e) {
    let fileReader = new FileReader();
    fileReader.onload = (e) => {
      this.formGroup.controls["file"].setValue(fileReader.result)
    }
    fileReader.readAsText(e.target.files[0]);
  }

  onSubmit(): void {
    console.log("Submitting data");
    console.log(this.formGroup.value);
    this.dataService.submit_data(this.formGroup.value);
    this.heatmapInfoService.img_loaded(false);
  }

}
