
//regresar data y total
var is_authenticated = false;
var ventana = $("#ventana");

function reoverData(){
}

var stylesFlex = {
	display:'flex',
	width:'100%'

};

var dataS = new kendo.data.DataSource({
	serverPaging: true,
	serverSorting: true,
	pageSize:10,
	transport:{
		read: {
			cache: false,
			type: "GET",
			url: '/listado/',
			contentType: "application/json; charset=utf-8",
            dataType: 'json',
            complete: function(e){
            	//ListaProductos.componentWillMount();
            		ReactDOM.unmountComponentAtNode(document.getElementById('contenedor'))
            	 ReactDOM.render(
            	 	<ListaProductos 
            	 	style={stylesFlex}
            	 	reload={true}
            	 	 />
            	 	,	
            	 	document.getElementById('contenedor')
            	 	);
				
				
			},	
		},
		parameterMap: function (options, operation) {
            if (operation == 'read')
                return {
                    take: options.take,
                    skip: options.skip,
                    filter: options.filter,
                    sort: options.sort,
                    search : $("#search").val(),
                    subcategoria : $("#selected").val()
                }
        }
	},
	requestStart: function() {

		var valorsearch = $("#search").val();
		if(multi && valorsearch){
			multi.dataSource.data([]);
			$("#selected").val('');

		}

        //kendo.ui.progress($("#products"), true);
    },
    requestEnd: function() {
        //kendo.ui.progress($("#products"), false);
    },
    change: function() {
        //$("#products").html(kendo.render(template, this.view()));
    },
    schema: {
                data: function (data) {
                	
                	is_authenticated = data.is_authenticated;
                    return data.Data;
                },
                total: function (data) {
                    return data.Total;
                },
                
            }
});






var ProductoSmall = React.createClass({
	getInitialState: function(){
		return {
			
		}
	},
	eachItem: function(propiedad, i){
		
		return(
			<li>{propiedad.propiedad}</li>
			)
	},
	is_authenticated: function()
	{
		
		if(is_authenticated)
			return(
						<div>
						
						</div>
					)
	},
	render: function(){
		
		this.props.props;
		return (
			
			<div className="ed-item tablet-30 web-25 main-center art">
				<div className="contenedor-producto">
					<a href="#">
						<div className="image-responsive producto-img main-center">
						<img className="image-box" src={this.props.imgurl} />
						</div>
						<div className="producto-titulo">
						<span>{this.props.nombre}</span>
						</div>
						<div className="producto-prop">
						<ul>
						{
							
							this.props.props.map(this.eachItem)
							
						}
						</ul>
						</div>
					</a>
				</div>
				
				{
					this.is_authenticated()
				}
				
				
					
				
			</div>
			
			);
	}
});



var ListaProductos = React.createClass({
	getInitialState:function() {
	    return {
	        productos : []  
	    };
	},
	componentWillMount: function() {
	      //dataS.read();
	      var self = this;

	      //if(dataS.hasChanges()){
	      //	debugger;
	      //}

	      //Promise.resolve(dataS.data())
	      //.then(function(result){
	      //	result=dataS.data();
	      	
	      //	for (var i = 0; i < result.length; i++) {

	      //		var _producto = result[i]
	      //		self.add(_producto);
	      //	}
	      //})
	      //.catch(function(er){
	      //	console.log(er);
	      //})
	      
	      
	},
	loadData: function(){
		var self = this;

	      //if(dataS.hasChanges()){
	      	
	      //}

	      //Promise.resolve(dataS.data())
	      //.then(function(result){
	      	result=dataS.data();
	      	this.setState({
	      		productos : result
	      	})
	      	for (var i = 0; i < result.length; i++) {

	      		//var _producto = result[i]
	      		//self.add(_producto);
	      	}
	      //})
	      //.catch(function(er){
	      	//console.log(er);
	      //})
	},
	eachItem: function(producto, i){
		
		//if(producto.imgs.length > 0)
			
		var img = "/static/img/noicon.jpg";//producto.imgs.length > 0 ? producto.imgs[0].url : "static/img/noicon.jpg"; 
		return(
			<ProductoSmall key={i}
			nombre={producto.nombre}
			props = {producto.props}
			imgurl = {img}
			index={i}
			>
			</ProductoSmall>
			)
	},
	add:function (producto) {
		var arr = this.state.productos;
		arr.push(producto);
		this.setState({
			productos:arr
		});
	},
	check: function(){
		if(this.props.reload){
			this.props.reload = false;
			this.loadData();
		}
	},
	render: function(){
		return (
			// <div className="content">
			// 	<div className="side">
			// 	<h2>{this.props.nombre}</h2>
			// 		<SideBar/>
			// 	</div>
			 	<div style={stylesFlex} className="">
					<div className="ed-container base-100">
						{
							this.check()
						}					
						{	
							this.state.productos.map(this.eachItem)
											
						}
					</div>
				</div>
			//</div>
			)
	}
});




function abrirAdd()
{
	
	if(!ventana.data("kendoWindow")){
		ventana.kendoWindow({
			title:"Agregar Producto",
			content:'/producto_add/',
			iframe:true,
			width:656,
			height:525,
			modal:true,
	}).data("kendoWindow").center().open();
	}else{
		ventana.data("kendoWindow").refresh('/producto_add/').center().open();
	}
}

$("#botton_add").kendoButton({
	spriteCssClass: 'k-icon k-i-plus',
	click: function(){
		abrirAdd();
	}
});

$("#search").keypress(function(e){
	if (e.charCode===13) {
		//dataS.read();	
		dataS.page(1);
	}
	
});

$("#btngo").kendoButton({
	click:function(){
		//alert(entro);
		dataS.read();
	}
});

//ReactDOM.render(<ListaProductos nombre="verguita" />, document.getElementById('contenedor'));


var pager = $("#pager").kendoPager({
	autoBind: true,
	dataSource:dataS,
	input:true,
	pageSizes: [5,10,25],
	change: function(){
		//<ListaProductos nombre = "Verga" />;
	}
}).data("kendoPager");



dataS.read();
