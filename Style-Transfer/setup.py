# Copyright 2020 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A setuptools based setup module for magenta."""

from setuptools import find_packages
from setuptools import setup

# Bit of a hack to parse the version string stored in version.py without
# executing __init__.py, which will end up requiring a bunch of dependencies to
# execute (e.g., tensorflow, pretty_midi, etc.).
# Makes the __version__ variable available.
with open('magenta/version.py') as in_file:
  exec(in_file.read())  # pylint: disable=exec-used

REQUIRED_PACKAGES = [
    'absl-py',
    'apache-beam[gcp] >= 2.14.0',
    'dm-sonnet',
    'imageio',
    'librosa >= 0.6.2',
    'matplotlib >= 1.5.3',
    'mido == 1.2.6',
    'mir_eval >= 0.4',
    'note-seq',
    'numba < 0.50',  # temporary fix for librosa import
    'numpy',
    'Pillow >= 3.4.2',
    'pretty_midi >= 0.2.6',
    'pygtrie >= 2.3',
    'python-rtmidi >= 1.1, < 1.2',  # 1.2 breaks us
    'scikit-image',
    'scipy >= 0.18.1',
    'six >= 1.12.0',
    'sk-video',
    'sox >= 1.3.7',
    'tensor2tensor',
    'tensorflow',
    'tensorflow-datasets',
    'tensorflow-probability',
    'tf_slim',
    'wheel',
]

EXTRAS_REQUIRE = {
    'onsets_frames_realtime': [
        'pyaudio',
        'colorama',
        'tflite',
    ],
    'test': [
        'pylint',
        'pytest',
    ]
}

# pylint:disable=line-too-long
CONSOLE_SCRIPTS = [
    'magenta.interfaces.midi.magenta_midi',
    'magenta.interfaces.midi.midi_clock',
    'magenta.checkpoint.arbitrary_image_stylization.arbitrary_image_stylization_evaluate',
    'magenta.checkpoint.arbitrary_image_stylization.arbitrary_image_stylization_train',
    'magenta.checkpoint.arbitrary_image_stylization.arbitrary_image_stylization_with_weights',
    'magenta.checkpoint.arbitrary_image_stylization.arbitrary_image_stylization_distill_mobilenet',
    'magenta.checkpoint.drums_rnn.drums_rnn_create_dataset',
    'magenta.checkpoint.drums_rnn.drums_rnn_generate',
    'magenta.checkpoint.drums_rnn.drums_rnn_train',
    'magenta.checkpoint.image_stylization.image_stylization_create_dataset',
    'magenta.checkpoint.image_stylization.image_stylization_evaluate',
    'magenta.checkpoint.image_stylization.image_stylization_finetune',
    'magenta.checkpoint.image_stylization.image_stylization_train',
    'magenta.checkpoint.image_stylization.image_stylization_transform',
    'magenta.checkpoint.improv_rnn.improv_rnn_create_dataset',
    'magenta.checkpoint.improv_rnn.improv_rnn_generate',
    'magenta.checkpoint.improv_rnn.improv_rnn_train',
    'magenta.checkpoint.gansynth.gansynth_train',
    'magenta.checkpoint.gansynth.gansynth_generate',
    'magenta.checkpoint.melody_rnn.melody_rnn_create_dataset',
    'magenta.checkpoint.melody_rnn.melody_rnn_generate',
    'magenta.checkpoint.melody_rnn.melody_rnn_train',
    'magenta.checkpoint.music_vae.music_vae_generate',
    'magenta.checkpoint.music_vae.music_vae_train',
    'magenta.checkpoint.nsynth.wavenet.nsynth_generate',
    'magenta.checkpoint.nsynth.wavenet.nsynth_save_embeddings',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_create_dataset',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_create_dataset_maps',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_create_tfrecords',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_infer',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_train',
    'magenta.checkpoint.onsets_frames_transcription.onsets_frames_transcription_transcribe',
    'magenta.checkpoint.onsets_frames_transcription.realtime.onsets_frames_transcription_realtime',
    'magenta.checkpoint.performance_rnn.performance_rnn_create_dataset',
    'magenta.checkpoint.performance_rnn.performance_rnn_generate',
    'magenta.checkpoint.performance_rnn.performance_rnn_train',
    'magenta.checkpoint.pianoroll_rnn_nade.pianoroll_rnn_nade_create_dataset',
    'magenta.checkpoint.pianoroll_rnn_nade.pianoroll_rnn_nade_generate',
    'magenta.checkpoint.pianoroll_rnn_nade.pianoroll_rnn_nade_train',
    'magenta.checkpoint.polyphony_rnn.polyphony_rnn_create_dataset',
    'magenta.checkpoint.polyphony_rnn.polyphony_rnn_generate',
    'magenta.checkpoint.polyphony_rnn.polyphony_rnn_train',
    'magenta.checkpoint.rl_tuner.rl_tuner_train',
    'magenta.checkpoint.sketch_rnn.sketch_rnn_train',
    'magenta.scripts.convert_dir_to_note_sequences',
    'magenta.tensor2tensor.t2t_datagen',
    'magenta.tensor2tensor.t2t_decoder',
    'magenta.tensor2tensor.t2t_trainer',
]
# pylint:enable=line-too-long

setup(
    name='magenta',
    version=__version__,  # pylint: disable=undefined-variable
    description='Use machine learning to create art and music',
    long_description='',
    url='https://magenta.tensorflow.org/',
    author='Google Inc.',
    author_email='magenta-discuss@gmail.com',
    license='Apache 2',
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='tensorflow machine learning magenta music art',

    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRAS_REQUIRE,
    entry_points={
        'console_scripts': ['%s = %s:console_entry_point' % (n, p) for n, p in
                            ((s.split('.')[-1], s) for s in CONSOLE_SCRIPTS)],
    },

    include_package_data=True,
    package_data={
        'magenta': ['checkpoint/image_stylization/evaluation_images/*.jpg'],
    },
)
