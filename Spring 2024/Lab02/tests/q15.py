test = {
  'name': '15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(powers_of_2 == 2 ** np.arange(15))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
