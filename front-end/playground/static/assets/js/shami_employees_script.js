$(document).ready(function() {
  $("#example").DataTable({
    aaSorting: [],
    responsive: true,

    columnDefs: [
      {
        responsivePriority: 1,
        targets: 0
      },
      {
        responsivePriority: 2,
        targets: -1
      }
    ]
  });

  $(".dataTables_filter input")
    .attr("placeholder", "Search here...")
    .css({
      margin: "20px 10px 10px 10px",
      width: "350px",
      height: "50px",
      display: "inline-block",
      color: "red",
      fontSize: "12px",
      background: "white"
    });

  $('[data-toggle="tooltip"]').tooltip();
});