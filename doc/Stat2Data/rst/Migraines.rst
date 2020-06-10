========= ===============
Migraines R Documentation
========= ===============

Migraines and TMS
-----------------

Description
~~~~~~~~~~~

Effects of transcranial magnetic stimulation (TMS) on migraine headaches

Format
~~~~~~

A data frame with 2 observations on the following 4 variables.

``Group``
   Treatment group (``Placebo`` or ``TMS``)

``Yes``
   Count of number of patients that were pain-free in each group

``No``
   Count of number of patients that had pain in each group

``Trials``
   Number of patients in each group

Details
~~~~~~~

A study investigated whether a handheld device that sends a magnetic
pulse into a person's head might be an effective treatment for migraine
headaches. Researchers recruited 200 subjects who suffered from
migraines and randomly assigned them to receive either the TMS
(transcranial magnetic stimulation) treatment or a sham (placebo)
treatment from a device that did not deliver any stimulation. Subjects
were instructed to apply the device at the onset of migraine symptoms
and then assess how they felt two hours later. This dataset is a two-way
table of the results.

This dataset was called TMS in the first edition.

Source
~~~~~~

Based on results in R. B. Lipton, et al, (2010) "Single-pulse
Transcranial Magnetic Stimulation for Acute Treatment of Migraine with
Aura: A Randomised, Double-blind, Parallel-group, Shamcontrolled Trial,"
Lancet Neurology, 9(4):373-380.