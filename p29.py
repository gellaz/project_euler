#!/usr/bin/env python
# coding: utf-8

min_range, max_range = 2, 100
accepted_range = [i for i in range(min_range, max_range+1)]
result_set = {i**j for i in accepted_range for j in accepted_range}
print('Number of distinct terms: {}'.format(len(result_set)))