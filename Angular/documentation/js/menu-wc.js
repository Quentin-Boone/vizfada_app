'use strict';

customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">viz-fa-da documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                                <li class="link">
                                    <a href="properties.html" data-type="chapter-link">
                                        <span class="icon ion-ios-apps"></span>Properties
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-toggle="collapse" ${ isNormalMode ?
                                'data-target="#modules-links"' : 'data-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link" >AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' : 'data-target="#xs-components-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' :
                                            'id="xs-components-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' }>
                                            <li class="link">
                                                <a href="components/AboutComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AboutComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/AppComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CanvasComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CanvasComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CarouselComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CarouselComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ControllerComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ControllerComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/EpistackComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >EpistackComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ExperimentComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ExperimentComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ExperimentsListComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ExperimentsListComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/FilterComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >FilterComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HeaderComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HeaderComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HeatmapComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HeatmapComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HighlightComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HighlightComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/LegendComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >LegendComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MainComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >MainComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MenuComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >MenuComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MetadataTableComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >MetadataTableComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/PlotlyComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >PlotlyComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ViewComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ViewComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#pipes-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' : 'data-target="#xs-pipes-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' }>
                                            <span class="icon ion-md-add"></span>
                                            <span>Pipes</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="pipes-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' :
                                            'id="xs-pipes-links-module-AppModule-1ceb9c9a2c121d0c9220d1c1bcd77e9905aad64e4a152a485afe02be07473781919d905db4349c7d7b5eef9fd293fb2aa56d81f19b14ff8a3d3dc06d603a6fb0"' }>
                                            <li class="link">
                                                <a href="pipes/BetterNamesPipe.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >BetterNamesPipe</a>
                                            </li>
                                            <li class="link">
                                                <a href="pipes/GetPipe.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GetPipe</a>
                                            </li>
                                            <li class="link">
                                                <a href="pipes/SafeHTMLPipe.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >SafeHTMLPipe</a>
                                            </li>
                                            <li class="link">
                                                <a href="pipes/SafePipe.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >SafePipe</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AppRoutingModule.html" data-type="entity-link" >AppRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/IconsModule.html" data-type="entity-link" >IconsModule</a>
                            </li>
                </ul>
                </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#components-links"' :
                            'data-target="#xs-components-links"' }>
                            <span class="icon ion-md-cog"></span>
                            <span>Components</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="components-links"' : 'id="xs-components-links"' }>
                            <li class="link">
                                <a href="components/HLFilterComponent.html" data-type="entity-link" >HLFilterComponent</a>
                            </li>
                        </ul>
                    </li>
                        <li class="chapter">
                            <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#directives-links"' :
                                'data-target="#xs-directives-links"' }>
                                <span class="icon ion-md-code-working"></span>
                                <span>Directives</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                            <ul class="links collapse " ${ isNormalMode ? 'id="directives-links"' : 'id="xs-directives-links"' }>
                                <li class="link">
                                    <a href="directives/HostDirective.html" data-type="entity-link" >HostDirective</a>
                                </li>
                            </ul>
                        </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#classes-links"' :
                            'data-target="#xs-classes-links"' }>
                            <span class="icon ion-ios-paper"></span>
                            <span>Classes</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="classes-links"' : 'id="xs-classes-links"' }>
                            <li class="link">
                                <a href="classes/CastTextUrl.html" data-type="entity-link" >CastTextUrl</a>
                            </li>
                            <li class="link">
                                <a href="classes/CustomReuseStrategy.html" data-type="entity-link" >CustomReuseStrategy</a>
                            </li>
                        </ul>
                    </li>
                        <li class="chapter">
                            <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#injectables-links"' :
                                'data-target="#xs-injectables-links"' }>
                                <span class="icon ion-md-arrow-round-down"></span>
                                <span>Injectables</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                            <ul class="links collapse " ${ isNormalMode ? 'id="injectables-links"' : 'id="xs-injectables-links"' }>
                                <li class="link">
                                    <a href="injectables/DataService.html" data-type="entity-link" >DataService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/EpistackService.html" data-type="entity-link" >EpistackService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/ExperimentService.html" data-type="entity-link" >ExperimentService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/HeatmapInfoService.html" data-type="entity-link" >HeatmapInfoService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/RequestOptionsService.html" data-type="entity-link" >RequestOptionsService</a>
                                </li>
                            </ul>
                        </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#interfaces-links"' :
                            'data-target="#xs-interfaces-links"' }>
                            <span class="icon ion-md-information-circle-outline"></span>
                            <span>Interfaces</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? ' id="interfaces-links"' : 'id="xs-interfaces-links"' }>
                            <li class="link">
                                <a href="interfaces/Article.html" data-type="entity-link" >Article</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/DataJSON.html" data-type="entity-link" >DataJSON</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Fields.html" data-type="entity-link" >Fields</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/FieldValues.html" data-type="entity-link" >FieldValues</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/File.html" data-type="entity-link" >File</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Folder.html" data-type="entity-link" >Folder</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Ontology.html" data-type="entity-link" >Ontology</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Organization.html" data-type="entity-link" >Organization</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/RouteStorageObject.html" data-type="entity-link" >RouteStorageObject</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/TextUnit.html" data-type="entity-link" >TextUnit</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/TextUrl.html" data-type="entity-link" >TextUrl</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#miscellaneous-links"'
                            : 'data-target="#xs-miscellaneous-links"' }>
                            <span class="icon ion-ios-cube"></span>
                            <span>Miscellaneous</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="miscellaneous-links"' : 'id="xs-miscellaneous-links"' }>
                            <li class="link">
                                <a href="miscellaneous/typealiases.html" data-type="entity-link">Type aliases</a>
                            </li>
                            <li class="link">
                                <a href="miscellaneous/variables.html" data-type="entity-link">Variables</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});