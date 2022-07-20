import { Component, OnInit, TemplateRef, ViewChild, ElementRef } from '@angular/core';

import { DatatableComponent } from '@swimlane/ngx-datatable';

import { DataService } from '../data.service';

type Column = {
  'name': string;
  'cellTemplate': TemplateRef<any>;
  'headerTemplate': TemplateRef<any>;
  'width': number;
};

@Component({
  selector: 'app-metadata-table',
  templateUrl: './metadata-table.component.html',
  styleUrls: ['./metadata-table.component.css']
})
export class MetadataTableComponent implements OnInit {
  @ViewChild('cellTemplate', { static: true }) cellTemplate: TemplateRef<any>;
  @ViewChild('headerTemplate') headerTemplate: TemplateRef<any>;
  @ViewChild(DatatableComponent) table: DatatableComponent;
  
  private DEFAULT_COLS: string[] = ["Accession", "Target", "Cell type", "Breed", "Health Status", "Sex"];
  private DEFAULT_MINWIDTH: number = 20;
  public selectedCols: string[];
  public cols: any[];
  public data: Object[];
  public loading: boolean = true;
  public selectedExperiments: Object[];
  public datacols: Column[];
  public allColumns: Column[];
  public allRows = [];
  
  objectKeys = Object.keys;
  isString(val): boolean { return typeof val === 'string'; };
  filterTextUrl(obj: Object): Object {
    let exclude = ['text', 'url'];
    return Object.keys(obj)
      .filter(key => !exclude.includes(key))
      .reduce((cur, key) => {
        cur[key] = obj[key];
        return cur;
    }, {});};
    makeurl(exp: string): string {
      return '/experiment/' + exp;
    }

  constructor(private dataService: DataService, private elementRef: ElementRef) { }

  ngOnInit(): void {
    this.dataService.submittedData.subscribe(
      (data) => {
        console.log("Updating metadata table...", data);
        this.get_metadata(data);
      },
      (err) => console.error(err)
    );
  }
  
  get_metadata(formData: Object): void {
    this.dataService.get_meta('table', formData).subscribe(
      (data) => {
        this.cols = data["columns"];
        this.data = data["data"];
        this.datacols = data["columns-datatable"].map((obj: {"name": string}): Column => ({ "name": obj.name, "cellTemplate": this.cellTemplate, "headerTemplate": this.headerTemplate, "width": this.DEFAULT_MINWIDTH }));
        this.allColumns = this.datacols;
        this.datacols = this.datacols.filter((obj: Column) => this.DEFAULT_COLS.includes(obj.name));
        this.datacols = this.datacols.sort((a: Column, b: Column) => {
          const indexA: number = this.DEFAULT_COLS.indexOf(a.name);
          const indexB: number = this.DEFAULT_COLS.indexOf(b.name);
          if (indexA < indexB || indexB === -1)
             return -1;
          if (indexA > indexB || indexA === -1)
             return 1;
          return 0;
        });
        console.log(this.datacols);
        this.adjustColumnMinWidth();
        this.allRows = [...this.data];
        console.log("Metadata columns and data", this.cols, this.data);
      },
      (err) => console.error(err),
      () => this.loading = false
    )
  }

  toggle(col) {
    const isChecked = this.isChecked(col);

    if (isChecked) {
      this.datacols = this.datacols.filter(c => {
        return c.name !== col.name;
      });
    } else {
      this.datacols = [...this.datacols, col];
    }

    this.adjustColumnMinWidth();
  }

  isChecked(col) {
    //console.log(col.name, "checked ? ", (this.datacols.find(c => {
    //  return c.name === col.name;
    //}) !== undefined));
    return (
      this.datacols.find(c => {
        return c.name === col.name;
      }) !== undefined
    );
  }

  adjustColumnMinWidth() {
    console.log("Adjusting column widths")
    const element = this.elementRef.nativeElement as HTMLElement;
    const rows = element.getElementsByTagName("datatable-body-row");
    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("datatable-body-cell");
      for (let k = 0; k < cells.length; k++) {
        const cell = cells[k];
        const cellSizer = cell.children[0].children[0] as HTMLElement;
        const sizerWidth = cellSizer.getBoundingClientRect().width + 20;
        if (this.datacols[k].width < sizerWidth) {
          this.datacols[k].width = sizerWidth;
        }
      }
    }
    this.table.recalculate();
}

  updateFilter(event, column) {
    const val = event.target.value.toLowerCase();

    // filter our data
    const temp = this.allRows.filter(function (d) {
      for (let v of d[column]){
        if (typeof(v) === 'string') {
          return v.toLowerCase().indexOf(val) !== -1 || !val;
        } else {
          return v['text'].toLowerCase().indexOf(val) !== -1 || !val;
        }
      }
    });
      //return d[column].toLowerCase().indexOf(val) !== -1 || !val;

    // update the rows
    this.data = temp;
    // Whenever the filter changes, always go back to the first page
    this.table.offset = 0;
  }

}
