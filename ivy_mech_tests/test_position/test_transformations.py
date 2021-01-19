"""
Collection of tests for homogeneous co-ordinate functions
"""

# global
import ivy_mech
import numpy as np
import ivy_mech_tests.helpers as helpers

# local
from ivy_mech_tests.test_position.position_data import PositionTestData

ptd = PositionTestData()


def test_make_coordinates_homogeneous():
    for lib, call in helpers.calls:
        if call is helpers.mx_graph_call:
            # mxnet symbolic does not fully support array slicing
            continue
        assert np.allclose(call(ivy_mech.make_coordinates_homogeneous, ptd.cartesian_coords),
                           ptd.cartesian_coords_homo, atol=1e-6)
        assert np.allclose(call(ivy_mech.make_coordinates_homogeneous, ptd.batched_cartesian_coords),
                           ptd.batched_cartesian_coords_homo, atol=1e-6)


def test_make_transformation_homogeneous():
    for lib, call in helpers.calls:
        if call is helpers.mx_graph_call:
            # mxnet symbolic does not fully support array slicing
            continue
        assert np.allclose(call(ivy_mech.make_transformation_homogeneous, ptd.ext_mat), ptd.ext_mat_homo, atol=1e-6)
        assert np.allclose(call(ivy_mech.make_transformation_homogeneous, ptd.batched_ext_mat),
                           ptd.batched_ext_mat_homo, atol=1e-6)
