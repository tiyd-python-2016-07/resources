var $abilities = $('#abilities')

$.ajax({
  url: '/api/abilities'
}).done(function(response) {
  if (response.count > 0) {
    response.results.forEach(function(result) {
      // make a table row
      var $tr = $('<tr>')

      var $name = $('<td>').text(result.name).appendTo($tr)

      $('<td>').text(result.description).appendTo($tr)

      $('<td>').text(result.power_level).appendTo($tr)

      $name.click(function() {
        var abilityName = $name.text()

        $name.empty()

        var $form = $('<form>').appendTo($name)

        var $input = $('<input type="text">').val(abilityName)

        $input.click(function() {
          return false;
        })

        $input.appendTo($form)

        $form.submit(function() {
          var abilityName = $input.val()

          $.ajax({
            method: 'PUT',
            url: '/api/abilities/' + result.id + '/',
            data: {
              name: abilityName,
              description: result.description,
              power_level: result.power_level
            }
          })

          $name.empty();
          $name.text(abilityName)

          return false;
        })
      })

      $tr.appendTo($abilities)
    })
  }
})
