#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 56. Merge Intervals# 

# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result_intervals = []
        intervals.sort(key=lambda interval: interval.start)
        for interval in intervals:
            if interval.start > interval.end:
                intervals.remove(interval)
        length = len(intervals)
        for i in range(length):
            if result_intervals == []:
                result_intervals.append(intervals[i])
            else:
                current_len = len(result_intervals)
                if result_intervals[current_len - 1].start <= intervals[i].start <= result_intervals[
                    current_len - 1].end:
                    result_intervals[current_len].end = max(intervals[i].end, result_intervals[current_len - 1].end)
                else:
                    result_intervals.append(intervals[i])
        return result_intervals
